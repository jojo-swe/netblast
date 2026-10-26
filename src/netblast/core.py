from __future__ import annotations

from collections import deque


def blast_radius(graph: dict[str, list[str]], changed: list[str]) -> dict[str, int]:
    """Return shortest dependency distance from every changed node."""
    distance = {node: 0 for node in changed}
    queue = deque(changed)
    while queue:
        node = queue.popleft()
        for dependent in graph.get(node, []):
            if dependent not in distance:
                distance[dependent] = distance[node] + 1
                queue.append(dependent)
    return distance


def invert(graph: dict[str, list[str]]) -> dict[str, list[str]]:
    """Flip a depends-on graph into the node-to-dependents form ``blast_radius`` expects."""
    inverted: dict[str, list[str]] = {}
    for node, targets in graph.items():
        for target in targets:
            inverted.setdefault(target, []).append(node)
    return inverted
