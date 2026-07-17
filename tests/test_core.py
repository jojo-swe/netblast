from netblast import blast_radius


def test_blast_radius_tracks_dependency_distance() -> None:
    graph = {"router-a": ["switch-b"], "switch-b": ["service-c"]}
    assert blast_radius(graph, ["router-a"]) == {
        "router-a": 0,
        "switch-b": 1,
        "service-c": 2,
    }
