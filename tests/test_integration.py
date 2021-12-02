from fixtures import (
    EXAMPLE_PACKAGE_JSON1,
    EXAMPLE_PYPROJECT_TOML1,
    EXAMPLE_README_MD1,
    EXAMPLE_README_RST1,
    EXAMPLE_POETS_JSON1,
)
from poetspy.poets import (
    get_dir_info,
    SOURCE_PACKAGE_JSON,
    SOURCE_PROJECT_TOML,
    SOURCE_README_MD,
    SOURCE_README_RST,
    SOURCE_POETS_JSON,
)


def test_readme_md(tmpdir):
    readmeMd = tmpdir.join("README.MD")
    readmeMd.write(EXAMPLE_README_MD1)
    assert get_dir_info(str(tmpdir)) == {
        SOURCE_README_MD: {
            "title": "PoetsPy",
            "subtitle": "A great python ls alternative",
        }
    }


def test_pyproject_toml(tmpdir):
    pyprojectToml = tmpdir.join("pyproject.toml")
    pyprojectToml.write(EXAMPLE_PYPROJECT_TOML1)
    assert get_dir_info(str(tmpdir)) == {
        SOURCE_PROJECT_TOML: {
            "title": "poetspy",
            "subtitle": "A small cli util to show project directories",
        }
    }


def test_poets_json(tmpdir):
    poetsJson = tmpdir.join(".poets.json")
    poetsJson.write(EXAMPLE_POETS_JSON1)
    assert get_dir_info(str(tmpdir)) == {
        SOURCE_POETS_JSON: {"title": "Hanasu", "subtitle": "A p2p chat app"}
    }


def test_package_json(tmpdir):
    packageJson = tmpdir.join("package.json")
    packageJson.write(EXAMPLE_PACKAGE_JSON1)
    assert get_dir_info(str(tmpdir)) == {
        SOURCE_PACKAGE_JSON: {
            "title": "h5ai",
            "subtitle": "Modern HTTP web server index.",
        }
    }


def test_readme_rst(tmpdir):
    readmeRst = tmpdir.join("README.rst")
    readmeRst.write(EXAMPLE_README_RST1)
    assert get_dir_info(str(tmpdir)) == {
        SOURCE_README_RST: {
            "title": "pingtop",
            "subtitle": "",
        }
    }
