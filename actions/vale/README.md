# vale

This action can be used in the following manner:

```yaml
jobs:
  vale:
    runs-on: ubuntu-slim
    permissions:
      checks: write
      contents: read
    steps:
      - uses: razekmh/.github/actions/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. Vale is a lightweight job, so
the `ubuntu-slim` runner is a fine (lower-cost) default; keep
`runs-on: ubuntu-latest` only if the job needs a full VM.

By default only Vale **errors** are reported and fail the job, as GitHub check
annotations (`github-check` reporter, which needs `checks: write`). Optional
inputs:

```yaml
jobs:
  vale:
    runs-on: ubuntu-slim
    permissions:
      checks: write
      contents: read
    steps:
      - uses: razekmh/.github/actions/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          min-alert-level: warning # suggestion, warning or error (default)
          reporter: github-pr-review # default github-check
          vale-flags: "" # extra flags for vale
          vale-version: 3.26.0 # Vale CLI version (default pinned)
```

Lowering `min-alert-level` can exceed reviewdog's limit of 10 annotations per
step, which fails the job regardless of severity.
