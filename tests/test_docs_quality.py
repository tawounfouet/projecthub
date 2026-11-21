"""Synthetic positive and negative controls for the documentation validator."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import docs_quality as dq


def metadata(doc_id: str = "DOC-01", status: str = "draft", classification: str = "public") -> str:
    return ("---\n" + f"id: {doc_id}\ntitle: Fixture\nversion: '0.1.0'\n"
            + f"status: {status}\nclassification: {classification}\nupdated_at: '2026-11-21'\n"
            + "---\n\n# Fixture\n")


class DocsQualityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("README.md", "# Home\n[Docs](docs/README.md)\n")
        self.write("docs/README.md", "# Docs\n")
        self.write("docs/example.md", metadata())
        for name, prefix, width, maximum, first, end in dq.REGISTRIES:
            lines = [f"## {first}. Canonical\n", "| ID | Label |\n", "|---|---|\n"]
            lines += [f"| `{prefix}-{i:0{width}d}` | Test |\n" for i in range(1, maximum + 1)]
            lines += [f"\n## {end}. Other\n", f"A citation `{prefix}-001` is not an extra entry.\n"]
            self.write(name, metadata(name.replace("/", "-")[:-3]) + "\n" + "".join(lines))

    def write(self, path: str, content: str) -> None:
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")

    def test_valid_repository_passes(self) -> None:
        self.assertEqual(dq.validate(self.root), [])

    def test_missing_frontmatter_fails(self) -> None:
        self.write("docs/another.md", "# No frontmatter")
        self.assertTrue(any("frontmatter manquant" in x for x in dq.validate(self.root)))

    def test_internal_classification_fails(self) -> None:
        self.write("docs/example.md", metadata(classification="INTERNAL"))
        self.assertTrue(any("classification non publique" in x for x in dq.validate(self.root)))

    def test_invalid_yaml_fails(self) -> None:
        self.write("docs/example.md", "---\nid: [unterminated\n---\n")
        self.assertTrue(any("frontmatter invalide" in x for x in dq.validate(self.root)))

    def test_duplicate_document_id_fails(self) -> None:
        self.write("docs/another.md", metadata())
        self.assertTrue(any("id duplique" in x for x in dq.validate(self.root)))

    def test_nonstandard_status_fails(self) -> None:
        self.write("docs/example.md", metadata(status="APPROVED_BY_BOT"))
        self.assertTrue(any("statut hors cycle" in x for x in dq.validate(self.root)))

    def test_missing_registry_id_fails(self) -> None:
        name = dq.REGISTRIES[0][0]
        file = self.root / name
        file.write_text(file.read_text().replace("| `PH-OPEN-010` | Test |\n", ""))
        self.assertTrue(any("manque=[10]" in x for x in dq.validate(self.root)))

    def test_duplicate_canonical_row_fails(self) -> None:
        name = dq.REGISTRIES[2][0]
        file = self.root / name
        file.write_text(file.read_text().replace("| `MVP-UJ-02` | Test |", "| `MVP-UJ-01` | Test |"))
        self.assertTrue(any("doublons=[1]" in x for x in dq.validate(self.root)))

    def test_broken_link_fails(self) -> None:
        self.write("docs/README.md", "[Missing](not-here.md)\n")
        self.assertTrue(any("cible absente" in x for x in dq.validate(self.root)))

    def test_wrong_case_link_fails(self) -> None:
        self.write("docs/README.md", "[Incorrect case](Example.md)\n")
        self.assertTrue(any("casse incorrecte" in x for x in dq.validate(self.root)))

    def test_html_image_missing_fails(self) -> None:
        self.write("README.md", '<img src="docs/missing.png" alt="test">\n')
        self.assertTrue(any("cible absente" in x for x in dq.validate(self.root)))

    def test_fenced_fake_links_ignored(self) -> None:
        self.write("docs/README.md", "```md\n[Fake](missing.md)\n```\n")
        self.assertEqual(dq.validate(self.root), [])

    def test_baseline_exception_is_path_scoped(self) -> None:
        self.write("docs/another.md", metadata("DOC-02", dq.BASELINE_STATUS))
        self.assertTrue(any("statut hors cycle" in x for x in dq.validate(self.root)))

    def test_legacy_allowlist_is_path_scoped(self) -> None:
        self.write("docs/reports/audit-2026-11-21/INDEX.md", "# Legacy snapshot\n")
        self.assertEqual(dq.validate(self.root), [])
        self.write("docs/reports/audit-2026-11-21/UNLISTED.md", "# New file\n")
        self.assertTrue(any("frontmatter manquant" in x for x in dq.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
