#!/usr/bin/env python3

import os
import json
import re
import toml
from typing import Union

import click
import marko


SOURCE_PACKAGE_JSON = "packageJson"
SOURCE_PROJECT_TOML = "pyprojectToml"
SOURCE_README_MD = "readmeMd"
SOURCE_README_RST = "readmeRst"

DESCRIPTION_SOURCE_PRIORITY = [
    SOURCE_PACKAGE_JSON,
    SOURCE_PROJECT_TOML,
    SOURCE_README_RST,
    SOURCE_README_MD,
]


parser = marko.parser.Parser()


def get_string_from_ast(node: marko.inline.InlineElement, base=0) -> str:
    # run again on string
    if isinstance(node, marko.inline.RawText):
        k = get_string_from_ast(node.children, base + 1)
    # use space to replace linebreaks in order to save space
    elif isinstance(node, marko.inline.LineBreak):
        k = " "
    # skip image alt texts
    elif isinstance(node, marko.inline.Image):
        return ""
    elif isinstance(node, str):
        k = node
    else:
        k = "".join([get_string_from_ast(t, base + 1) for t in node.children])
    return k


def get_description_from_readmeMd(markdown: str) -> str:
    ast = parser.parse(markdown)
    description = {}
    for block in ast.children:
        # skip blank lines
        if isinstance(block, marko.block.BlankLine):
            continue
        # skip html stuff
        # TODO: add html tag parsing
        elif isinstance(block, marko.block.HTMLBlock):
            continue
        # read headings
        elif isinstance(block, marko.block.Heading) and block.inline_children:
            if "title" in description:
                continue
            description["title"] = get_string_from_ast(block).strip()
        # read descriptions
        else:
            description["subtitle"] = get_string_from_ast(block).strip()
            break

    return description


def get_description_from_packageJson(package: str) -> str:
    """Gets description about a directory using its node package.json"""
    v = json.loads(package)
    description = {}
    if "title" in v:
        description["name"] = v["title"].strip()
    if "description" in v:
        description["subtitle"] = v["description"].strip()
    return description


def get_description_from_pyprojectToml(string: str) -> str:
    meta = toml.loads(string)
    description = {}
    if "tool" in meta:
        if "poetry" in meta["tool"]:
            if "name" in meta["tool"]["poetry"]:
                description["title"] = meta["tool"]["poetry"]["name"].strip()
            if "description" in meta["tool"]["poetry"]:
                description["subtitle"] = meta["tool"]["poetry"]["description"].strip()
    return description


def get_description_from_readmeRst(string: str) -> str:
    rx = re.compile(r"([\S])\1{3,}")
    lines = [l.strip() for l in string.split("\n")]
    lastline = ""
    for line in lines:
        if rx.match(line):
            return {"title": lastline}
        lastline = line


def join_title_and_subtitle(title: str, subtitle: str) -> str:
    final_description = ""
    if title:
        final_description += click.style(title, bold=True, underline=True)

    if subtitle:
        if len(subtitle) > 82:
            subtitle = subtitle[:82] + "..."
        if final_description:
            final_description += " - " + subtitle
        else:
            final_description += subtitle
    return final_description


def get_dir_info(path: str) -> Union[str, None]:
    """Get description of dir"""
    p = os.listdir(path)
    descriptions = {}
    # TODO: pass file path instead of file content for optimization possibility
    for i in p:
        if i.lower() == "readme.md":
            with open(os.path.join(path, i)) as f:
                descriptions[SOURCE_README_MD] = get_description_from_readmeMd(f.read())
        elif i.lower() == "package.json":
            with open(os.path.join(path, i)) as f:
                descriptions[SOURCE_PACKAGE_JSON] = get_description_from_packageJson(
                    f.read()
                )
        elif i.lower() == "pyproject.toml":
            with open(os.path.join(path, i)) as f:
                descriptions[SOURCE_PROJECT_TOML] = get_description_from_pyprojectToml(
                    f.read()
                )
        elif i.lower() == "readme.rst":
            with open(os.path.join(path, i)) as f:
                descriptions[SOURCE_README_RST] = get_description_from_readmeRst(
                    f.read()
                )

    title = ""
    subtitle = ""
    for source in DESCRIPTION_SOURCE_PRIORITY:
        if source in descriptions:
            if "title" in descriptions[source]:
                if descriptions[source]["title"]:
                    title = descriptions[source]["title"]
                    break
    for source in DESCRIPTION_SOURCE_PRIORITY:
        if source in descriptions:
            if "subtitle" in descriptions[source]:
                if descriptions[source]["subtitle"]:
                    subtitle = descriptions[source]["subtitle"]
                    break
    # if SOURCE_PACKAGE_JSON in descriptions:
    #     return join_title_and_subtitle(descriptions[SOURCE_PACKAGE_JSON])
    # elif SOURCE_PROJECT_TOML in descriptions:
    #     return join_title_and_subtitle(descriptions[SOURCE_PROJECT_TOML])
    # elif SOURCE_READ_ME in descriptions:
    #     return join_title_and_subtitle(descriptions[SOURCE_READ_ME])

    return join_title_and_subtitle(title, subtitle)


@click.command()
def main():
    d = "."
    dirs = [o for o in os.listdir(d) if os.path.isdir(os.path.join(d, o))]
    u = {}
    for a in dirs:
        u[a + "/"] = get_dir_info(a)

    for l in u.keys():
        if u[l]:
            click.echo(click.style(l, fg="blue") + " " + u[l])
        else:
            click.echo(click.style(l, fg="blue"))


if __name__ == "__main__":
    main()
