import io
import sys

import marko
import pytest

from fixtures import (
    EXAMPLE_README_MD1,
    EXAMPLE_README_MD2,
    EXAMPLE_README_MD3,
    EXAMPLE_README_MD4,
    EXAMPLE_README_RST1,
)
from poets import (
    file_to_string,
    get_description_from_readmeMd,
    get_description_from_readmeRst,
    get_string_from_markdown_ast,
    is_badge_line,
    join_title_and_subtitle,
    logger,
)


def test_readme_md():
    assert get_description_from_readmeMd(EXAMPLE_README_MD1) == {
        "title": "PoetsPy",
        "subtitle": "A great python ls alternative",
    }
    assert get_description_from_readmeMd(EXAMPLE_README_MD2) == {
        "title": "Title",
        "subtitle": "this is just a random readme",
    }
    assert get_description_from_readmeMd(EXAMPLE_README_MD3) == {
        "title": "Node.JS Chat",
        "subtitle": "This is a node.js chat application powered by SockJS and Express that provides the main functions you'd expect from a chat, such as emojis, private messages, an admin system, etc.",
    }
    assert get_description_from_readmeMd(EXAMPLE_README_MD4) == {
        "title": "Color LS",
        "subtitle": "A Ruby script that colorizes the ls output with color and icons. Here are the screenshots of working example on an iTerm2 terminal (Mac OS), oh-my-zsh with powerlevel9k theme and powerline nerd-font + awesome-config font with the Solarized Dark color theme.",
    }


def test_path_reader(tmp_path):
    u = tmp_path / "test1.txt"
    u.write_text("ABCDefgHijklmn")
    assert file_to_string(str(u)) == "ABCDefgHijklmn"

    v = tmp_path / "test2.txt"
    v.write_text("happy birthday!你好!")
    assert file_to_string(v) == "happy birthday!你好!"


def test_title_selection(snapshot):
    assert (
        join_title_and_subtitle("Poetspy", "Another ls alternative", False)
        == "Poetspy - Another ls alternative"
    )
    assert (
        join_title_and_subtitle("Poetspy", "j" * 99, False)
        == "Poetspy - " + "j" * 82 + "..."
    )
    assert (
        join_title_and_subtitle("Poetspy", "Another ls alternative", True) == snapshot
    )


def test_readme_rst():
    i = io.StringIO(EXAMPLE_README_RST1)
    assert get_description_from_readmeRst(i) == {"title": "pingtop"}


def test_get_readme_text():
    parser = marko.parser.Parser()

    ast = parser.parse("**Hello** *World!*").children[0]
    assert get_string_from_markdown_ast(ast) == "Hello World!"

    ast = parser.parse("Hello ![img](inserted) *World!*").children[0]
    assert get_string_from_markdown_ast(ast) == "Hello  World!"

    ast = parser.parse("Hello [link](ref) *World!*").children[0]
    assert get_string_from_markdown_ast(ast) == "Hello link World!"

    ast = parser.parse("# Hello [World!](there)").children[0]
    assert get_string_from_markdown_ast(ast) == "Hello World!"

    ast = parser.parse("![one](src) ![2](src)").children[0]
    assert is_badge_line(ast) == True

    ast = parser.parse("![one](src) some text![2](src)").children[0]
    assert is_badge_line(ast) == False

    ast = parser.parse("[![one](src)](other_source) ![2](src)").children[0]
    assert is_badge_line(ast) == True
