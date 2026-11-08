# Safe-Settings

[Safe-Settings](https://github.com/github-community-projects/safe-settings) is a
way to manage policy-as-code and apply repository settings across the account. A
private GitHub App (`razekmh-safe-settings`) is used by the
[GitHub Action](../.github/workflows/safe-settings.yaml) to apply the settings
on every push to `main` and every 4 hours. On pull requests it runs as a dry run
(`FULL_SYNC_NOP`) and reports what would change.

## Managed repositories

Only the repositories listed under `restrictedRepos.include` in
[deployment.yaml](deployment.yaml) are managed: `.github`, `mini-rag`,
`razekmh.github.io` and `talks`. Entries are plain names or
[minimatch](https://github.com/isaacs/minimatch) globs (not regular
expressions). Install the GitHub App on the same repositories; Safe-Settings
only processes repositories the App is installed on.

## Configuration Files

There are four types of settings that can be applied:

- [Deployment](https://raw.githubusercontent.com/github-community-projects/safe-settings/refs/heads/main-enterprise/docs/sample-settings/sample-deployment-settings.yml)
  which defines deployment and runtime settings.
- [Account](https://raw.githubusercontent.com/github-community-projects/safe-settings/refs/heads/main-enterprise/docs/sample-settings/settings.yml)
  which can be used to define account-level settings.
- [Repository](https://raw.githubusercontent.com/github-community-projects/safe-settings/refs/heads/main-enterprise/docs/sample-settings/repo.yml)
  which can be used to define repo-level settings.
- [Suborganisation](https://raw.githubusercontent.com/github-community-projects/safe-settings/refs/heads/main-enterprise/docs/sample-settings/suborg.yml)
  which can be used to define suborganisation-level settings.

The precedence order for configuration is `repository` > `suborganisation` >
`account`.

## The Settings in This Repository

### Deployment

The [deployment settings](deployment.yaml) limit Safe-Settings to the managed
repositories above.

### Account

The [account settings](account.yaml) apply to every managed repository: merge
commits and squash merges allowed (rebase merges off), auto-merge and "update
branch" on, branches deleted after merge, and wiki, discussions and downloads
off.

### Suborganisation

The [suborganisation settings](suborgs/rulesets.yaml) define
[rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
for every managed repository:

- **Default**: the default branch can't be deleted or force-pushed.
- **Release tags**: `v*.*.*` tags can't be deleted or moved. The floating major
  tag (e.g. `v0`) is deliberately not covered, because
  [tags.yaml](../.github/workflows/tags.yaml) force-moves it on each release.

Account-level `rulesets` apply to the account itself rather than to individual
repositories, so they are set through a suborganisation that matches every
repository:

```yaml
suborgrepos:
  - "*"
```

Further explanation can be found in the
[Safe-Settings issues](https://github.com/github-community-projects/safe-settings/issues/553#issuecomment-2552578978).

## Setting up the GitHub App

One-time setup (the workflow is skipped until `SAFE_SETTINGS_APP_ID` exists):

1. Create the App at <https://github.com/settings/apps/new>:
   - **Name:** `razekmh-safe-settings`; **Homepage URL:** this repository
   - **Webhook:** untick **Active** (the GitHub Action does the syncing)
   - **Repository permissions** (from the
     [Safe-Settings deployment docs](https://raw.githubusercontent.com/github-community-projects/safe-settings/refs/heads/main-enterprise/docs/deploy.md)):
     Actions: Read-only; Administration, Checks, Commit statuses, Contents,
     Custom properties, Environments, Issues, Pull requests and Variables: Read
     & Write; Metadata: Read-only. The organisation permissions don't apply to a
     personal account.
   - **Where can this App be installed?** Only on this account
2. On the App's page, note the **App ID** and **Client ID**, generate a **client
   secret**, and generate a **private key** (`.pem` download).
3. **Install App** → _Only select repositories_ → the managed repositories.
4. Add the variables and secrets to this repository:

   ```sh
   gh variable set SAFE_SETTINGS_APP_ID --body "<App ID>"
   gh variable set SAFE_SETTINGS_GITHUB_CLIENT_ID --body "<Client ID>"
   gh variable set SAFE_SETTINGS_GH_ORG --body razekmh
   gh secret set SAFE_SETTINGS_GITHUB_CLIENT_SECRET   # paste the client secret
   gh secret set SAFE_SETTINGS_PRIVATE_KEY < ~/Downloads/razekmh-safe-settings.*.private-key.pem
   ```

5. Run **Safe Settings Sync** from the Actions tab (`workflow_dispatch`) and
   check the log, then delete the downloaded `.pem` file.
