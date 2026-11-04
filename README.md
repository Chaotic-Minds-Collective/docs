# Chaotic Minds Collective Handbook

This repository holds the public organizational handbook for Chaotic Minds Collective. It is not an employee handbook, HR portal, internal engineering runbook, or product API reference.

## How the site works

The handbook is plain markdown rendered by Jekyll (minima theme, dark skin) on GitHub Pages. Every push to `main` deploys automatically. There is no build tooling to install and no external service involved.

- Content pages live in folders (`about/`, `divisions/`, `governance/`, `projects/`, `brand/`, `technology/`) plus the root `index.md`.
- `_config.yml` controls the theme and the header navigation.
- `changelog.md` is the organization-wide changelog.

## Editing conventions

- Plain markdown only. No MDX, no custom components.
- Every page starts with front matter: `title`, `description`, `layout: page`.
- Internal links use the page URL (`/divisions/solutions.html`, `/about/`).
- Changelog entries use `## <date>` for the entry, `### <project>` for sections inside it, and a `>` blockquote for deployment-status notes.
- See `AGENTS.md` for writing style, public-content boundaries, and approval discipline.

## Changelog workflow

New entries are appended at the top of `changelog.md` following the format above. Each entry records merged source changes separately from deployment status, consistent with the November 3, 2026 entry.

## Tests

`tests/test_handbook_content.py` runs with the standard library only:

```sh
python3 -m unittest discover tests
```
