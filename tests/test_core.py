from netblast import blast_radius, invert


def test_blast_radius_tracks_dependency_distance() -> None:
    graph = {"router-a": ["switch-b"], "switch-b": ["service-c"]}
    assert blast_radius(graph, ["router-a"]) == {
        "router-a": 0,
        "switch-b": 1,
        "service-c": 2,
    }


def test_blast_radius_stops_on_cycles() -> None:
    assert blast_radius({"a": ["b"], "b": ["a"]}, ["a"]) == {"a": 0, "b": 1}


def test_blast_radius_keeps_shortest_path() -> None:
    graph = {"a": ["b", "d"], "b": ["d"]}
    assert blast_radius(graph, ["a"]) == {"a": 0, "b": 1, "d": 1}


def test_blast_radius_handles_changed_node_missing_from_graph() -> None:
    assert blast_radius({"a": ["b"]}, ["x"]) == {"x": 0}


def test_blast_radius_starts_all_changed_nodes_at_zero() -> None:
    graph = {"a": ["c"], "b": ["c"], "c": ["d"]}
    assert blast_radius(graph, ["a", "b"]) == {"a": 0, "b": 0, "c": 1, "d": 2}


def test_blast_radius_with_no_changes_is_empty() -> None:
    assert blast_radius({"a": ["b"]}, []) == {}


def test_invert_turns_depends_on_into_dependents() -> None:
    depends_on = {"switch-b": ["router-a"], "service-c": ["switch-b"]}
    dependents = {"router-a": ["switch-b"], "switch-b": ["service-c"]}
    assert invert(depends_on) == dependents
    assert blast_radius(invert(depends_on), ["router-a"]) == blast_radius(dependents, ["router-a"])
