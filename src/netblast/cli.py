from __future__ import annotations

import argparse
import json

from .core import blast_radius


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="netblast", description="Show how far a change spreads through a dependency graph."
    )
    parser.add_argument("graph", help='JSON file of {"node": ["dependent", ...]}')
    parser.add_argument("changed", nargs="+", help="changed node names")
    args = parser.parse_args(argv)
    with open(args.graph, encoding="utf-8") as f:
        graph = json.load(f)
    result = blast_radius(graph, args.changed)
    for node, distance in sorted(result.items(), key=lambda item: (item[1], item[0])):
        print(f"{distance}  {node}")
    return 0
