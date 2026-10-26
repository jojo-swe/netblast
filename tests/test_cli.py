import json
from pathlib import Path

import pytest

from netblast.cli import main


def test_main_prints_distances_sorted(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    graph = tmp_path / "graph.json"
    graph.write_text(json.dumps({"router-a": ["switch-b", "fw-z"], "switch-b": ["service-c"]}))
    assert main([str(graph), "router-a"]) == 0
    assert capsys.readouterr().out.splitlines() == [
        "0  router-a",
        "1  fw-z",
        "1  switch-b",
        "2  service-c",
    ]
