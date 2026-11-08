# Composite Actions

A set of
[composite actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
that can be called by other workflows.

## Pinning

Reference a commit SHA with the version in a trailing comment, on **one line**:

```yaml
- uses: razekmh/.github/actions/linting@<sha> # v1
```

Keep the `uses:` line on a single line. Renovate only updates the SHA when it
can read the whole reference on one line — a folded `uses: >-` over two lines is
missed (this caused a missed bump in razekmh/talks).
