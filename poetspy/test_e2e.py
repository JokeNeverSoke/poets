import os
from click.testing import CliRunner
from poets import main
from fixtures import (
    EXAMPLE_README_MD,
    EXAMPLE_PYPROJECT_TOML,
    EXAMPLE_PACKAGE_JSON,
    EXAMPLE_README_RST,
)

runner = CliRunner()


def test_output(snapshot, tmpdir):
    d = ["abc", "some-thing", "yeah_yeah", "poetspy"]
    dd = [tmpdir.mkdir(i) for i in d]
    dd[0].join("package.json").write(EXAMPLE_PACKAGE_JSON)
    dd[1].join("readme.md").write(EXAMPLE_README_MD)
    dd[1].join("README.rst").write(EXAMPLE_README_RST)
    dd[2].join("readme.rst").write(EXAMPLE_README_RST)
    dd[2].join("pyproject.toml").write(EXAMPLE_PYPROJECT_TOML)
    os.chdir(tmpdir)

    assert runner.invoke(main).stdout == snapshot