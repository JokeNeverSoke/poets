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
