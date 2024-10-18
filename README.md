# Example `uv`workspace project

> [!IMPORTANT]
> The `flake.nix` and `flake.lock` files are the way I install `uv` and `python`. Most people have these installed globally on their system, and can just ignore those two files.

## How I made this

1. Create `uv_test_project` folder; run `uv init` inside it.
2. Create `package_one` and `package_two` folders; un `uv init` inside them.

Each step modifies the `pyproject.toml` at the root level (`uv_test_project`).

### Adding dependencies
If `package_one` depends on `numpy`, then go into `package_one` and run `uv add numpy`
