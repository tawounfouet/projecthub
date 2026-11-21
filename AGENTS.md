# AGENTS.md - ProjectHub

## Repo shape
- Documentation-only research repo in Discovery; no application source, package manifests, build/test/lint commands, or GitHub Actions workflows. Do not claim features, ADRs, E0 demos, or E1 pilots are approved or implemented; E1 remains `No-Go`.
- The Django/DRF + Next.js/React/TypeScript/PostgreSQL stack and 13-domain map in `README.md` and the architecture baseline are target proposals, not delivered code.
- `docs/README.md` is the public doc index. `docs/00-context/` through `docs/06-validation/` hold the 25 sanitized Discovery Baseline editions; later `docs/07-architecture/`, `docs/reports/`, and post-Discovery docs are additions outside that count.

## Confidentiality first
- `resources/` is a local private archive: 46 Markdown files, 24 PNGs, plus `resources/internal/docs/**`, `public-drafts/` and `INVENTAIRE.json` (which declares 32 Markdown files and 20 PNGs). It is not tracked by Git; never commit it or copy its content, paths, names, quotes, or inventory into public docs, issues, or PRs.
- Public docs are manually rewritten, sanitized editions. Publication is never an automatic sync from the private corpus and requires explicit maintainer approval; an AI agent cannot authorize third-party or sensitive content.
- `docs/07-architecture/ProjectHub-Architecture-Engineering-Baseline-V1.0-2026-11-21.md` is committed and now classified `public` under `PH-DEC-019`, while remaining `DRAFT / PROPOSED - NOT APPROVED`. Do not treat that publication decision as technical or business approval; see `docs/07-architecture/README.md` and audit bug B1.
- The `resources/` and `archives/` ignore rules are now versioned in `.gitignore`. Verify them with `git check-ignore -v resources/INVENTAIRE.json` after a fresh clone; audit bug B9 is closed.

## Documentation conventions
- Substantive `docs/**/*.md` use YAML frontmatter with `id`, `title`, `version`, `status`, `classification`, `updated_at`; status cycle is `draft|in-review|approved|superseded`, classification is `public` for public editions. READMEs are exempt.
- Preserve stable IDs and ranges. Canonical registries: `PH-OPEN-001..030` in `docs/00-context/04-open-questions.md`, `PH-BLG-001..045` in `docs/05-mvp/02-prioritized-backlog.md`, `MVP-UJ-01..10` in `docs/05-mvp/01-user-journeys.md`, `PH-REV-001..020` in `docs/06-validation/01-discovery-baseline-review.md`. Count first-column table rows only; ranges such as `PH-REQ-001..130` and repeated citations are not records.
- Public prose is mostly French. Keep index tables and document statuses in sync whenever docs change.

## Workflow
- Read `docs/PUBLICATION-POLICY.md` before content edits and `docs/COLLABORATION-BEST-PRACTICES.md` before PRs; both encode repo-specific review and publication rules.
- Work in a focused `docs/...` branch as a PR Draft, then mark Ready. A maintainer comment in Conversation is not a GitHub `APPROVED` review. PUBLIC-01 to PUBLIC-04 were squash merged; PRs #7 to #11 appear as two-parent merges in local history. Do not claim a universal rule; update the index after merge.
- Available preflight checks today: `git diff --check` and `git status --short` (including untracked and binary files). There is no configured doc-quality CI: `docs/07-architecture/01-documentation-quality-ci-plan.md` is `NOT_IMPLEMENTED`, not a script to run.
- Public issues must exclude private pilot/customer data, transcripts, credentials, and security findings; report security issues privately, as stated in `.github/ISSUE_TEMPLATE/`.

## Audit deliverables
- The audit lives in `docs/reports/audit-2026-11-21/`. `CODEBASE_ANALYSIS.md` defines bugs B1..B9; keep those IDs stable in every other audit document.
- `ANALYSE_CRITIQUE.md` is opinion, `RECOMMANDATIONS.md` is action, `DOCUMENTATION-SYSTEM.md` is descriptive, and `INDEX.md` is the navigation entry point.
- Check relative links between the five audit documents and `README.md` after any edit; see `docs/reports/audit-2026-11-21/INDEX.md`.

## Local agents, skills and commands
- `.agents/` holds the canonical, machine-independent agent definitions for this project: `ph-docs-guardian`, `ph-audit-reviewer`, `ph-sdlc-guide`, `ph-link-checker`, and `ph-commit-planner`.
- `.agents/skills/` holds the canonical skill definitions: `repo-audit`, `sdlc-orchestrator`, `git-hygiene`, `session-archive`, `docs-writer`, and `docs-reviewer`.
- `.agents/commands/` holds the canonical command definitions: `audit`, `sdlc`, `review`, `pr-review`, `docs`, `commit`, `archive`, and `link-check`.
- `.opencode/agents/`, `.opencode/skills/`, and `.opencode/commands/` hold thin OpenCode adapters that load those definitions. OpenCode auto-discovers files in `.opencode/`, not in `.agents/`.
- Keep each adapter pointing to its canonical file in `.agents/`. After adding or changing an adapter, quit and restart OpenCode; config is loaded once at startup.
- Local agents, skills, and commands never commit, push, open a PR, or approve publication without an explicit maintainer action.
