import os
import json

import pytest
from click.testing import CliRunner

from fixtures import (
    EXAMPLE_PACKAGE_JSON1,
    EXAMPLE_PYPROJECT_TOML1,
    EXAMPLE_README_MD1,
    EXAMPLE_README_RST1,
)
from poets import main as pt_main
from generate import main as ptg_main

runner = CliRunner()


@pytest.fixture
def project_dir(tmpdir):
    d = ["abc", "some-thing", "yeah_yeah", "poetspy"]
    dd = [tmpdir.mkdir(i) for i in d]
    dd[0].join("package.json").write(EXAMPLE_PACKAGE_JSON1)
    dd[1].join("readme.md").write(EXAMPLE_README_MD1)
    dd[1].join("README.rst").write(EXAMPLE_README_RST1)
    dd[2].join("readme.rst").write(EXAMPLE_README_RST1)
    dd[2].join("pyproject.toml").write(EXAMPLE_PYPROJECT_TOML1)
    return tmpdir


def test_output(snapshot, project_dir):
    o = runner.invoke(pt_main, [str(project_dir)]).output
    assert o == snapshot
    os.chdir(project_dir)
    assert o == runner.invoke(pt_main).output


def test_ansi_colors(snapshot, project_dir):
    assert runner.invoke(pt_main, [str(project_dir)], color=True).output == snapshot
    assert (
        runner.invoke(pt_main, [str(project_dir), "--no-ansi"], color=True).output
        == snapshot
    )


def test_dry_run(project_dir):
    assert runner.invoke(pt_main, [str(project_dir), "--dry"], color=True).output == ""
    assert runner.invoke(pt_main, [str(project_dir), "-D"], color=True).output == ""


def test_generate(tmpdir):
    p = tmpdir.mkdir("project")
    poetsJson = p.join(".poets.json")
    os.chdir(p)
    runner.invoke(ptg_main, ["title", "Hello World!"])
    assert json.loads(poetsJson.read()) == {"title": "Hello World!"}
    runner.invoke(ptg_main, ["title", "Hello World"])
    assert json.loads(poetsJson.read()) == {
        "title": "Hello World",
    }
    runner.invoke(ptg_main, ["des", "A description with typo"])
    assert json.loads(poetsJson.read()) == {
        "title": "Hello World",
        "subtitle": "A description with typo",
    }
    runner.invoke(ptg_main, ["des", "A description without typo"])
    assert json.loads(poetsJson.read()) == {
        "title": "Hello World",
        "subtitle": "A description without typo",
    }
    poetsJson.remove()
    runner.invoke(ptg_main, ["des", "A description without typo"])
    runner.invoke(ptg_main, ["title", "Yay"])
    assert json.loads(poetsJson.read()) == {
        "title": "Yay",
        "subtitle": "A description without typo",
    }
    os.chdir("..")
    assert (
        "project/ Yay - A description without typo"
        in runner.invoke(pt_main, ["--no-ansi"], color=True).output
    )


def test_poets_json_dir(tmpdir):
    p = tmpdir.mkdir("project")
    poetsJson = p.mkdir(".poets.json")
    os.chdir(p)
    result = runner.invoke(ptg_main, ["title", "Project"])
    assert "is a directory!" in result.output
    assert result.exit_code == 1
    result = runner.invoke(ptg_main, ["des", "Some project"])
    assert "is a directory!" in result.output
    assert result.exit_code == 1
