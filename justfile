_default:
    @just --list

fmt:
    black ./poetspy || poetry run black ./poetspy

install:
    poetry install

build:
    poetry build

publish: build
    poetry publish -u $PYPI_USERNAME -p $PYPI_PASSWORD

bump VERSION:
    echo {{VERSION}} | poetry run python3 bumpversion.py

test *FLAGS:
    poetry run pytest {{FLAGS}}

coverage:
    poetry run coverage run

report: coverage
    poetry run coverage report -m

report-html: coverage
    poetry run coverage html
    open htmlcov/index.html

