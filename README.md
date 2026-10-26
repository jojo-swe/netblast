# NetBlast

Estimate the blast radius of a network change from structured dependencies.

## Install

Requires Python 3.11 or newer.

```bash
python -m pip install -e ".[dev]"
```

## Quick start

```python
from netblast import blast_radius

blast_radius(
    {"router-a": ["switch-b"], "switch-b": ["service-c"]},
    ["router-a"],
)
# {"router-a": 0, "switch-b": 1, "service-c": 2}
```

## Graph semantics

Each graph key maps a node to the nodes that *depend on it*. Changed nodes are distance 0, and
every other value is the shortest hop count from any changed node. Unreachable nodes are left out
of the result, and cycles are safe. If your inventory lists what each node depends on instead,
flip it first with `invert`:

```python
from netblast import blast_radius, invert

blast_radius(invert({"switch-b": ["router-a"]}), ["router-a"])
# {"router-a": 0, "switch-b": 1}
```

## Command line

Write the graph as a JSON object of `{"node": ["dependent", ...]}` and pass one or more changed
nodes. Results print as `distance  node`, sorted by distance then name.

```bash
$ netblast graph.json router-a
0  router-a
1  switch-b
2  service-c
```

`python -m netblast` works the same way.

## Development

```bash
ruff check .
pytest
```

CI runs both on Python 3.11, 3.12 and 3.13.

## License

Apache-2.0
