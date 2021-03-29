_default:
    @just --list

fmt:
    black ./src || poetry run black ./src

install:
    poetry install

build:
    poetry build

publish: build
    poetry publish
