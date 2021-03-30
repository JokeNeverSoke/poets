from poets import get_dir_info
from fixtures import (
    EXAMPLE_README_MD,
    EXAMPLE_PYPROJECT_TOML,
    EXAMPLE_PACKAGE_JSON,
    EXAMPLE_README_RST,
)


def test_readme_md(tmpdir):
    readmeMd = tmpdir.join("README.MD")
    readmeMd.write(EXAMPLE_README_MD)
    assert get_dir_info(str(tmpdir)) == ("PoetsPy", "A great python ls alternative")


def test_pyproject_toml(tmpdir):
    pyprojectToml = tmpdir.join("pyproject.toml")
    pyprojectToml.write(EXAMPLE_PYPROJECT_TOML)
    assert get_dir_info(str(tmpdir)) == (
        "poetspy",
        "A small cli util to show project directories",
    )


def test_package_json(tmpdir):
    packageJson = tmpdir.join("package.json")
    packageJson.write(EXAMPLE_PACKAGE_JSON)
    assert get_dir_info(str(tmpdir)) == ("h5ai", "Modern HTTP web server index.")


def test_readme_rst(tmpdir):
    readmeRst = tmpdir.join("README.rst")
    readmeRst.write(EXAMPLE_README_RST)
    assert get_dir_info(str(tmpdir)) == ("pingtop", "")
