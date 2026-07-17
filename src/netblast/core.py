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
