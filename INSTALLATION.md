# Installation — `<tenant>-wl`

One-time setup for a new white-label repository, publishing, and local development.

This pack is product-specific. The console loads `@<tenant>/wl`; the API imports `wl` (Python distribution `<tenant>-wl`).

---

## Create the repository

1. On GitHub, open [renglo/example-wl](https://github.com/renglo/example-wl) → **Use this template** → create `<tenant>-wl` in your org (usually private).
2. Clone:

```bash
git clone git@github.com:<ORG>/<tenant>-wl.git
cd <tenant>-wl
```

3. Rename packages:

`package.json`:

```json
{
  "name": "@<tenant>/wl"
}
```

`pyproject.toml`: set the project name to `<tenant>-wl`. The import name stays `wl`.

4. Replace initial branding and copy (see [README.md](README.md) for who edits which files).

5. Commit and push to your team’s default branch (often `develop`).

---

## Repository layout

| Path | Role |
| --- | --- |
| `product.yaml` | Product package list (handles → python / npm names) |
| `package.json` | npm pack `@<tenant>/wl` |
| `pyproject.toml` | Python dist `<tenant>-wl`, import `wl` |
| `src/wl/__init__.py` | Python API (`app_name`, locales, logo paths) |
| `index.js` / `index.d.ts` | Console exports (logos, captions, locales) |
| `captions.js` | Short UI strings |
| `locales/*.json` | Translations and invite templates |
| `assets/*.png` | Logos and login background |
| `wl_build.py` | Stage `locales/`, `assets/`, `product.yaml` into the wheel |
| `.github/workflows/publish-*.yml` | Tag `v*` → registry publish |

---

## Publish

When changes on the default branch should reach shared environments, tag a release:

```bash
git tag v0.0.1
git push origin v0.0.1
```

GitHub Actions need `AWS_PUBLISH_ROLE_ARN`, `PUBLISHER_NAME`, and `AWS_REGION` (same as other product repos). npm publishes `@<tenant>/wl`; Python publishes `<tenant>-wl`.

Before a local wheel build:

```bash
python wl_build.py
python -m build
```

---

## Local development

**Console** — in env (see console templates):

```bash
VITE_WL_PACKAGE=@<tenant>/wl
```

A workspace checkout at `dev/<tenant>-wl` or `<tenant>-wl` can be resolved like any other `@*/wl` pack (`wl.local.ts`).

**API** — editable install:

```bash
pip install -e ../<tenant>-wl
python -c "import wl; print(wl.app_name)"
```

Editable installs read `locales/` and `assets/` from the repo root. Wheels use the copy staged under `src/wl/` (`python wl_build.py`).
