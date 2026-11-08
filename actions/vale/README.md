# vale

This action can be used in the following manner:

```yaml
jobs:
  vale:
    runs-on: ubuntu-slim
    steps:
      - uses: razekmh/.github/actions/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. Vale is a lightweight job, so
the `ubuntu-slim` runner is a fine (lower-cost) default; keep
`runs-on: ubuntu-latest` only if the job needs a full VM. If flags are required for vale,
then modify the above to:

```yaml
jobs:
  vale:
    runs-on: ubuntu-slim
    steps:
      - uses: razekmh/.github/actions/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          vale-flags: ""
```
