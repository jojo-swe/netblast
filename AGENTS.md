# AGENTS.md

## Purpose

NetBlast estimates how far a network change spreads through a directed dependency graph.

`blast_radius(graph, changed)` returns the shortest hop count from the changed set to every reachable node. Changed nodes are distance 0. Each graph entry maps a node to the nodes that depend on it:

```python
from netblast import blast_radius

blast_radius(
    {"router-a": ["switch-b"], "switch-b": ["service-c"]},
    ["router-a"],
)
# {"router-a": 0, "switch-b": 1, "service-c": 2}
```

## Layout

- `src/netblast/core.py` — breadth-first implementation of `blast_radius`, plus `invert`
- `src/netblast/__init__.py` — public API; re-exports `blast_radius` and `invert` in `__all__`
- `src/netblast/cli.py` — `netblast` command-line entry point (`main`)
- `src/netblast/__main__.py` — runs the CLI for `python -m netblast`
- `tests/test_core.py`, `tests/test_cli.py` — pytest tests
- `pyproject.toml` — package metadata, console script, Hatchling build, dev extras, Ruff and pytest settings
- `.github/workflows/ci.yml` — Ruff and pytest on Python 3.11, 3.12 and 3.13

## Commands

Requires Python 3.11 or newer.

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
netblast graph.json node...
```

CI runs the first three commands on Python 3.11, 3.12 and 3.13.

## Conventions

- Import the public function with `from netblast import blast_radius`. Add new public names to `__all__`.
- Keep edge direction as node to dependents. Do not walk the graph upstream. To use depends-on data, flip it with `invert()` before calling `blast_radius`.
- Graph JSON files are `{"node": ["dependent", ...]}` objects.
- Record the first distance found. Breadth-first search makes that the shortest path and also stops cycles.
- Annotate with Python 3.11+ types (`dict[str, list[str]]`, `list[str]`, `dict[str, int]`). Test functions return `None`.
- Ruff line length is 100, set in `pyproject.toml`. There is no extra Ruff rule selection.
- Version is `0.1.0`. License is Apache-2.0. The wheel package is `src/netblast` via Hatchling.
