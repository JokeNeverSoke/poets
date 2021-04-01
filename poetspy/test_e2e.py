import os

import pytest
from click.testing import CliRunner

from fixtures import (
    EXAMPLE_PACKAGE_JSON1,
    EXAMPLE_PYPROJECT_TOML1,
    EXAMPLE_README_MD1,
    EXAMPLE_README_RST1,
)
from poets import main

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
    o = runner.invoke(main, [str(project_dir)]).output
    assert o == snapshot
    os.chdir(project_dir)
    assert o == runner.invoke(main).output


def test_ansi_colors(snapshot, project_dir):
    assert runner.invoke(main, [str(project_dir)], color=True).output == snapshot
    assert (
        runner.invoke(main, [str(project_dir), "--no-ansi"], color=True).output
        == snapshot
    )


def test_dry_run(project_dir):
    assert runner.invoke(main, [str(project_dir), "--dry"], color=True).output == ""
    assert runner.invoke(main, [str(project_dir), "-D"], color=True).output == ""
