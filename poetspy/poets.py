#!/usr/bin/env python3

import os
import json
import toml
from typing import Union

import click
import marko


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


def get_description_from_markdown(markdown: str) -> str:
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
            description["title"] = get_string_from_ast(block)
        # read descriptions
        else:
            description["subtitle"] = get_string_from_ast(block)
            break

    return description


def get_description_from_packageJson(package: str) -> str:
    """Gets description about a directory using its node package.json"""
    v = json.loads(package)
    description = {}
    if "title" in v:
        description["name"] = v["title"]
    if "description" in v:
        description["subtitle"] = v["description"]
    return description


def get_description_from_pyprojectToml(string: str) -> str:
    meta = toml.loads(string)
    description = {}
    if "tool" in meta:
        if "poetry" in meta["tool"]:
            if "name" in meta["tool"]["poetry"]:
                description["title"] = meta["tool"]["poetry"]["name"]
            if "description" in meta["tool"]["poetry"]:
                description["subtitle"] = meta["tool"]["poetry"]["description"]
    return description


def join_title_and_subtitle(meta: dict) -> str:
    final_description = ""
    if "title" in meta:
        if meta["title"]:
            final_description += click.style(meta["title"], bold=True, underline=True)

    if "subtitle" in meta:
        if meta["subtitle"]:
            if len(meta["subtitle"]) > 82:
                meta["subtitle"] = meta["subtitle"][:82] + "..."
            if final_description:
                final_description += " - " + meta["subtitle"]
            else:
                final_description += meta["subtitle"]
    return final_description


def get_dir_info(path: str) -> Union[str, None]:
    """Get description of dir"""
    p = os.listdir(path)
    descriptions = {}
    for i in p:
        if i.lower() == "readme.md":
            with open(os.path.join(path, i)) as f:
                descriptions["readme"] = get_description_from_markdown(f.read())
        elif i.lower() == "package.json":
            with open(os.path.join(path, i)) as f:
                descriptions["packageJson"] = get_description_from_packageJson(f.read())
        elif i.lower() == "pyproject.toml":
            with open(os.path.join(path, i)) as f:
                descriptions["pyprojectToml"] = get_description_from_pyprojectToml(
                    f.read()
                )

    if "packageJson" in descriptions:
        return join_title_and_subtitle(descriptions["packageJson"])
    elif "pyprojectToml" in descriptions:
        return join_title_and_subtitle(descriptions["pyprojectToml"])
    elif "readme" in descriptions:
        return join_title_and_subtitle(descriptions["readme"])

    return


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
