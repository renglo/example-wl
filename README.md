# Product pack (template)

Public GitHub template ([renglo/example-wl](https://github.com/renglo/example-wl)). After **Use this template**, rename npm/Python packages to `@<tenant>/wl` and `<tenant>-wl` (see [INSTALLATION.md](INSTALLATION.md)).

This repository is the **single place** for product branding, messaging, and the list of packages the product ships. Console, API, and infrastructure read from the published pack; you change files here and merge through your normal Git workflow.

First-time repo setup, publishing, and local dev: **[INSTALLATION.md](INSTALLATION.md)**.

---

## Who changes what


| You are…         | You edit…                 | You usually do **not** touch…                             |
| ---------------- | ------------------------- | --------------------------------------------------------- |
| Graphic designer | `assets/`                 | `product.yaml`, `package.json`, code                      |
| Copy / messaging | `locales/`, `captions.js` | `assets/` (unless coordinating a rebrand), `product.yaml` |
| Developer        | `product.yaml`            | Version pins, deployment placement (operator / infra)     |


**Do not rename** files under `assets/` or change export names in `index.js`. Replace file **contents** only, unless a developer adds a new locale or asset slot.

After your change merges, someone tags a release when staging or production should pick it up (see [Publish](INSTALLATION.md#publish) in INSTALLATION.md).

---



## Graphic designer — logos and imagery

**Folder:** `assets/`


| File             | Where it appears              | Suggested size |
| ---------------- | ----------------------------- | -------------- |
| `small_logo.png` | Header, menu, small UI chrome | 500×500 px     |
| `large_logo.png` | Login screen mark             | 1000×1000 px   |
| `background.png` | Login background              | e.g. 1920×1080 |


Use PNG (or the same format already in the repo). Keep the **exact filenames** above so the console and npm pack keep resolving paths.

**Checklist**

1. Export replacements with the same names.
2. Drop them into `assets/` (overwrite the old files).
3. Open a pull request with only asset changes (or pair with copy if it is a full rebrand).
4. Preview locally if someone on the team runs the console with this checkout; otherwise rely on staging after release.

Invite emails attach `small_logo.png`. If the small mark changes, no other file rename is required.

---



## Copy and messaging — locales and captions

**Primary files:** `locales/*.json`, `captions.js`

### `locales/en.json` (and other languages)

This file drives UI strings and **transactional email** copy (for example team invites under `email.invite`). The API reads the same JSON through the `wl` Python package.

Typical keys:

- `appName` — product name shown across the UI and emails.
- Login and general UI strings (structure matches the template in this repo).
- `email.invite` — subject, body, and placeholders for invite messages (`{appName}`, `{team}`, `{inviter}`, `{code}`, etc.).

To add a language, copy the `en.json` pattern to `locales/<code>.json` and register that locale in `index.js` (ask a developer for the one-line export if you are unsure).

### `captions.js`

Short strings used in places that import captions directly. Keep wording **consistent** with `locales/en.json` where the same concept appears twice.

**Checklist**

1. Edit JSON in `locales/` (valid JSON: double quotes, no trailing commas).
2. Update `captions.js` if the same phrase lives there.
3. Pull request; mention if invite email copy changed so QA can send a test invite.
4. Tagged release ships copy to environments that install the pack from the registry.

You do **not** edit the console or API repos for product copy.

---



## Developer — product package list (`product.yaml`)

**File:** `product.yaml`

This is the **manifest** of packages the product should install: marketplace extensions, shared modules, and handler packs. Operators sync it into environment config; you maintain the list here in Git.

```yaml
packages:
  data:
    python: renglo-data
    npm: '@renglo/data'
  billing:
    python: acme-billing
    npm: '@acme/billing'
```


| Field                      | Meaning                                               |
| -------------------------- | ----------------------------------------------------- |
| Key (`data`, `billing`, …) | **Handle** — short name used in placement and tooling |
| `python`                   | Wheel name on the registry (omit if UI-only)          |
| `npm`                      | Scoped UI package (omit if API-only)                  |


**Include** anything the whole product should ship, even when no single repo imports it (for example a channel extension everyone gets in the marketplace).

**Do not list** platform packages (`renglo-lib`, `renglo-api`, `@renglo/console`, or this white-label pack).

**Do not add** version numbers or hub/peer placement. Versions come from the release train; placement is operator work after the handle exists.

If an extension imports another package in code, keep that dependency in the extension’s `pyproject.toml` / `package.json`. Use `product.yaml` when membership is a **product** decision, not only a library import.

**Checklist**

1. Add or update a block under `packages:` with the handle and registry names from the extension repo.
2. Pull request in **this** repository (no `*-bom` checkout required on your machine).
3. After merge, tell the operator a new handle may need **placement** before deploy.
4. Release train / registry pins for new packages are handled outside this file.

---



## Quick reference — all paths


| Path                                         | Owner                            |
| -------------------------------------------- | -------------------------------- |
| `assets/*.png`                               | Design                           |
| `locales/*.json`                             | Copy                             |
| `captions.js`                                | Copy                             |
| `product.yaml`                               | Developer (product manifest)     |
| `index.js`, `package.json`, `pyproject.toml` | Developer (structure / releases) |

