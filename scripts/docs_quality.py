#!/usr/bin/env python3
"""ProjectHub public documentation checks. No network, no automatic edits."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
import yaml

REQUIRED = ("id", "title", "version", "status", "classification", "updated_at")
STATES = {"draft", "in-review", "approved", "superseded"}
# Historical audit notes predate the frontmatter policy. This allowlist is
# narrow, public, and deliberately NOT a generic reports/ exemption.
LEGACY_NO_FRONTMATTER = {
    "docs/reports/audit-2026-11-21/ANALYSE_CRITIQUE.md",
    "docs/reports/audit-2026-11-21/CODEBASE_ANALYSIS.md",
    "docs/reports/audit-2026-11-21/DOCUMENTATION-SYSTEM.md",
    "docs/reports/audit-2026-11-21/INDEX.md",
    "docs/reports/audit-2026-11-21/RECOMMANDATIONS.md",
}
# Publication PH-DEC-019 did not approve the engineering baseline itself.
BASELINE_PATH = "docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md"
BASELINE_STATUS = "DRAFT / PROPOSED - NOT APPROVED"
REGISTRIES = (
    ("docs/00-context/04-open-questions.md", "PH-OPEN", 3, 30, 2, 6),
    ("docs/05-mvp/02-prioritized-backlog.md", "PH-BLG", 3, 45, 4, 5),
    ("docs/05-mvp/01-user-journeys.md", "MVP-UJ", 2, 10, 3, 4),
    ("docs/06-validation/01-discovery-baseline-review.md", "PH-REV", 3, 20, 6, 7),
)


def frontmatter(text: str) -> dict | None:
    m = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", text, re.S)
    if m is None:
        return None
    obj = yaml.safe_load(m.group(1))
    if not isinstance(obj, dict):
        raise ValueError("frontmatter YAML non mapping")
    return obj


def check_metadata(root: Path) -> list[str]:
    errors = []
    ids: dict[str, str] = {}
    for file in sorted((root / "docs").rglob("*.md")):
        rel = file.relative_to(root).as_posix()
        if file.name == "README.md" or rel in LEGACY_NO_FRONTMATTER:
            continue
        try:
            fm = frontmatter(file.read_text(encoding="utf-8"))
        except (UnicodeError, yaml.YAMLError, ValueError) as exc:
            errors.append(f"{rel}: frontmatter invalide ({type(exc).__name__})")
            continue
        if fm is None:
            errors.append(f"{rel}: frontmatter manquant")
            continue
        for name in REQUIRED:
            if name not in fm or fm[name] in (None, "", []):
                errors.append(f"{rel}: champ requis manquant {name}")
        doc_id = fm.get("id")
        if isinstance(doc_id, str) and doc_id.strip():
            if doc_id in ids:
                errors.append(f"{rel}: id duplique {doc_id} (aussi dans {ids[doc_id]})")
            ids[doc_id] = rel
        elif doc_id is not None:
            errors.append(f"{rel}: id doit etre une chaine non vide")
        if fm.get("classification") != "public":
            errors.append(f"{rel}: classification non publique")
        status = fm.get("status")
        if status not in STATES and not (rel == BASELINE_PATH and status == BASELINE_STATUS):
            errors.append(f"{rel}: statut hors cycle public")
        updated = fm.get("updated_at")
        if isinstance(updated, datetime):
            errors.append(f"{rel}: updated_at doit etre une date YYYY-MM-DD")
        elif isinstance(updated, date):
            pass
        elif not (isinstance(updated, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", updated)):
            errors.append(f"{rel}: updated_at invalide")
        else:
            try:
                date.fromisoformat(updated)
            except ValueError:
                errors.append(f"{rel}: updated_at invalide")
    return errors


def check_registries(root: Path) -> list[str]:
    errors = []
    for name, prefix, width, max_id, first, end in REGISTRIES:
        file = root / name
        if not file.is_file():
            errors.append(f"{name}: fichier de registre absent")
            continue
        text = file.read_text(encoding="utf-8")
        begin_match = re.search(rf"^##\s+{first}\.\s", text, re.M)
        end_match = re.search(rf"^##\s+{end}\.\s", text, re.M)
        if begin_match is None or end_match is None or end_match.start() <= begin_match.start():
            errors.append(f"{name}: bornes de section canonique introuvables")
            continue
        section = text[begin_match.end():end_match.start()]
        pattern = re.compile(rf"`?{re.escape(prefix)}-(\d{{{width}}})`?")
        values = []
        for line in section.splitlines():
            if not line.startswith("|"):
                continue
            first_cell = line.split("|", 2)[1].strip()
            m = pattern.fullmatch(first_cell)
            if m:
                values.append(int(m.group(1)))
        count = Counter(values)
        duplicates = sorted(n for n, c in count.items() if c > 1)
        missing = sorted(set(range(1, max_id + 1)) - set(values))
        extra = sorted(set(values) - set(range(1, max_id + 1)))
        if missing or duplicates or extra:
            errors.append(f"{name}: registre {prefix} manque={missing} doublons={duplicates} hors_plage={extra}")
    return errors


class _HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value and ((tag == "a" and key == "href") or (tag in ("img", "source") and key == "src")):
                self.links.append(value)

    handle_startendtag = handle_starttag


def _targets(md: MarkdownIt, content: str) -> list[str]:
    targets: list[str] = []
    for token in md.parse(content):
        candidates = [token] + (token.children or [])
        for child in candidates:
            if child.type == "link_open":
                targets.append(child.attrGet("href") or "")
            elif child.type == "image":
                targets.append(child.attrGet("src") or "")
            elif child.type in ("html_block", "html_inline"):
                html = _HTMLLinks()
                html.feed(child.content)
                targets.extend(html.links)
    return targets


def check_links(root: Path) -> list[str]:
    errors: list[str] = []
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    files = ([root / "README.md"] if (root / "README.md").is_file() else []) + list((root / "docs").rglob("*.md"))
    for file in sorted(files):
        rel = file.relative_to(root).as_posix()
        try:
            urls = _targets(md, file.read_text(encoding="utf-8"))
        except (UnicodeError, ValueError) as exc:
            errors.append(f"{rel}: Markdown illisible ({type(exc).__name__})")
            continue
        for url in urls:
            if not url or url.startswith(("#", "//")):
                continue
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue  # No external requests, no external URL validation.
            path = unquote(parsed.path)
            if not path:
                continue
            if path.startswith("/"):
                errors.append(f"{rel}: lien local absolu interdit ({path})")
                continue
            target = (file.parent / path).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{rel}: lien hors depot ({path})")
                continue
            if not target.exists():
                errors.append(f"{rel}: cible absente ou casse incorrecte ({path})")
    return errors


def validate(root: Path) -> list[str]:
    if not (root / "docs").is_dir():
        return ["docs/: dossier manquant"]
    return check_metadata(root) + check_registries(root) + check_links(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true", help="exit 1 on any validation error")
    args = parser.parse_args()
    issues = validate(args.root.resolve())
    for item in issues:
        print("ERROR:", item, file=sys.stderr)
    print(f"Documentation Quality: {len(issues)} anomalie(s)")
    return int(bool(issues) and args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
