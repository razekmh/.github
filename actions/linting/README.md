# linting

This action can be used in the following manner:

```yaml
jobs:
  linting:
    runs-on: ubuntu-slim
    steps:
      - uses: razekmh/.github/actions/linting@vx
        with:
          pre-commit-config: ./.pre-commit-config.yaml
```

where `x` is the `major` version of the action.

The action installs its own tooling (uv, prek, node), so the lightweight
`ubuntu-slim` runner is enough and bills lower — a good default while your
repo is private. Keep `runs-on: ubuntu-latest` if a job needs a full VM
(e.g. `github-pages/quarto` rendering or any Jupyter execution).
