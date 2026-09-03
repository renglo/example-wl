# example-wl

Public **GitHub template** for a console **white-label** package
(`@<tenant>/wl`). It supplies logos, captions, and language files that the
console loads as `@wl`.

Real systems rename this pack (for example Acme uses `@acme/wl`). The **filenames** under `assets/` and the export shape in `index.js` must stay the
same so the console keeps working.

---

## Create a new `<tenant>-wl` repository

You need a GitHub account that can create repositories in the **destination
organization**.

### 1. Create the repo from this template

1. Open this repository on GitHub:
  [renglo/example-wl](https://github.com/renglo/example-wl) .
2. Click **Use this template** → **Create a new repository**.
3. Choose:
  - **Owner:** the destination organization (or your user).
  - **Repository name:** `<tenant>-wl` (example: `apollo-wl`).
  - **Visibility:** usually **Private**.
4. Click **Create repository**.

You do **not** need any other local project layout to start.

### 2. Clone your new repo

```bash
git clone git@github.com:<ORG>/<tenant>-wl.git
cd <tenant>-wl
```

<tenant> is the name of the target system.

### 3. Rename the npm package

In `package.json`, set the name to your scope:

```json
{
  "name": "@<tenant>/wl"
}
```

Rules:

- Must match `@<tenant>/wl` (the console treats any `@*/wl` pack as white-label).
- Keep `"version"` starting at `0.0.1` (or whatever you will publish).



### 4. Replace branding files

**Keep these filenames.** Only replace the file contents.


| File                    | Used for                                    | Suggested size |
| ----------------------- | ------------------------------------------- | -------------- |
| `assets/small_logo.png` | Header and menu logo                        | 500×500 px     |
| `assets/large_logo.png` | Login mark                                  | 1000×1000 px   |
| `assets/background.png` | Login background                            | e.g. 1920×1080 |
| `locales/en.json`       | English copy (`appName`, login text)        | —              |
| `captions.js`           | Short strings — keep in sync with `en.json` | —              |


Add another language as `locales/<code>.json` and export it from `index.js`
(same pattern as `en`).

### 5. Commit and push

```bash
git add package.json captions.js locales assets
git commit -m "Brand <tenant> white-label pack"
git push origin main
```



### 6. Wire it into your system BOM

In your `<tenant>-bom` repo, either:

**Git pin** (CI clones this repo):

```json
"repos": {
  "mycompany/apollo-wl": {
    "url": "git@github.com:mycompany/apollo-wl.git",
    "commit": "<full sha>",
    "branch": "main"
  }
}
```

**Or npm pin** after you publish to CodeArtifact:

```json
"npm": {
  "@apollo/wl": "0.0.1"
}
```

Also set the console env so it loads your pack (deploy / `.env`):

```bash
VITE_WL_PACKAGE=@apollo/wl
```



### 7. Publish (optional)

`.github/workflows/publish-npm.yml` publishes to the publisher CodeArtifact when
you push a `v*` tag. Configure repo variables first (`AWS_PUBLISH_ROLE_ARN`,
`PUBLISHER_NAME`, `AWS_REGION`) the same way as other npm packages. Until then
you can ship via the git pin only.

---



## Package layout


| Path                                | Role                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------ |
| `package.json`                      | npm name `@<tenant>/wl`                                                        |
| `index.js` / `index.d.ts`           | Public exports (`smallLogo`, `largeLogo`, `background`, `captions`, `locales`) |
| `captions.js`                       | Short UI strings                                                               |
| `locales/*.json`                    | Locale files                                                                   |
| `assets/*.png`                      | Logos and login background                                                     |
| `.github/workflows/publish-npm.yml` | Tag → CodeArtifact publish                                                     |




## Local console development

Point the console at your pack with `VITE_WL_PACKAGE=@<tenant>/wl`. With a
workspace checkout named `<tenant>-wl` (or `dev/<tenant>-wl`), the console
resolver can pick it up the same way as other WL packs — see the console
`wl.local.ts` / env templates.