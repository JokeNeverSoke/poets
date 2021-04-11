from fixtures import (
    EXAMPLE_PACKAGE_JSON1,
    EXAMPLE_PYPROJECT_TOML1,
    EXAMPLE_README_MD1,
    EXAMPLE_README_RST1,
    EXAMPLE_POETS_JSON1,
)
from poets import get_dir_info


def test_readme_md(tmpdir):
    readmeMd = tmpdir.join("README.MD")
    readmeMd.write(EXAMPLE_README_MD1)
    assert get_dir_info(str(tmpdir)) == ("PoetsPy", "A great python ls alternative")


def test_pyproject_toml(tmpdir):
    pyprojectToml = tmpdir.join("pyproject.toml")
    pyprojectToml.write(EXAMPLE_PYPROJECT_TOML1)
    assert get_dir_info(str(tmpdir)) == (
        "poetspy",
        "A small cli util to show project directories",
    )


def test_poets_json(tmpdir):
    poetsJson = tmpdir.join(".poets.json")
    poetsJson.write(EXAMPLE_POETS_JSON1)
    assert get_dir_info(str(tmpdir)) == ("Hanasu", "A p2p chat app")


def test_package_json(tmpdir):
    packageJson = tmpdir.join("package.json")
    packageJson.write(EXAMPLE_PACKAGE_JSON1)
    assert get_dir_info(str(tmpdir)) == ("h5ai", "Modern HTTP web server index.")


def test_readme_rst(tmpdir):
    readmeRst = tmpdir.join("README.rst")
    readmeRst.write(EXAMPLE_README_RST1)
    assert get_dir_info(str(tmpdir)) == ("pingtop", "")
