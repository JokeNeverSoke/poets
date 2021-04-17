#!/usr/bin/env python3

import json
import os
import re
import sys
import threading
from queue import Queue

import click
import marko
import toml
from loguru import logger

LOGGING_LEVELS = [99, 50, 40, 30, 25, 20, 10, 5]

SOURCE_PACKAGE_JSON = "packageJson"
SOURCE_PROJECT_TOML = "pyprojectToml"
SOURCE_README_MD = "readmeMd"
SOURCE_README_RST = "readmeRst"
SOURCE_POETS_JSON = "poetsJson"

DESCRIPTION_SOURCE_PRIORITY = [
    SOURCE_POETS_JSON,
    SOURCE_PACKAGE_JSON,
    SOURCE_PROJECT_TOML,
    SOURCE_README_RST,
    SOURCE_README_MD,
]


def file_to_string(path: str) -> str:
    with open(path) as f:
        return f.read()


def is_badge_line(node: marko.block.Paragraph) -> bool:
    if not hasattr(node, "children"):
        return False
    for k in node.children:
        if isinstance(k, marko.inline.LineBreak):
            continue
        elif isinstance(k, marko.inline.Link):
            if (
                k.children
                and len(k.children) == 1
                and isinstance(k.children[0], marko.inline.Image)
            ):
                continue
            else:
                return True
        elif isinstance(k, marko.inline.Image):
            continue
        elif not get_string_from_markdown_ast(k).strip():
            continue
        else:
            logger.debug(
                "found non-badge element {} {}", get_string_from_markdown_ast(k), k
            )
            return False
    return True


def get_string_from_markdown_ast(node: marko.inline.InlineElement, base=0) -> str:
    # run again on string
    if isinstance(node, marko.inline.RawText):
        k = get_string_from_markdown_ast(node.children, base + 1)
    # use space to replace linebreaks in order to save space
    elif isinstance(node, marko.inline.LineBreak):
        k = " "
    # skip image alt texts
    elif isinstance(node, marko.inline.Image):
        k = ""
    # skip blocks
    elif isinstance(node, (marko.block.LinkRefDef, marko.block.ThematicBreak)):
        k = ""
    elif isinstance(node, marko.block.BlankLine):
        k = " "
    elif isinstance(node, str):
        k = node
    else:
        k = "".join([get_string_from_markdown_ast(t, base + 1) for t in node.children])
    return k


def get_description_from_readmeMd(markdown: str) -> str:
    parser = marko.parser.Parser()
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
        # skip lines with only images
        elif is_badge_line(block):
            continue
        # read headings
        # TODO: find title & subtitle on heading type (H1/H2/H3)
        elif (
            isinstance(block, (marko.block.Heading, marko.block.SetextHeading))
            and block.children
        ):
            if "title" in description:
                continue
            description["title"] = get_string_from_markdown_ast(block).strip()
        # read descriptions
        else:
            description["subtitle"] = get_string_from_markdown_ast(block).strip()
            logger.trace('read description "{}"', description["subtitle"])
            break

    return description


def get_description_from_packageJson(package: str) -> str:
    """Gets description about a directory using its node package.json"""
    v = json.loads(package)
    description = {}
    if "name" in v:
        description["title"] = v["name"].strip()
        logger.opt(colors=True).debug(
            f"found name in package.json <u>{description['title']}</u>"
        )
    if "description" in v:
        description["subtitle"] = v["description"].strip()
        logger.opt(colors=True).debug(
            f"found subtitle in package.json <u>{description['subtitle']}</u>"
        )
    return description


def get_description_from_pyprojectToml(string: str) -> str:
    meta = toml.loads(string)
    description = {}
    if "tool" in meta:
        if "poetry" in meta["tool"]:
            if "name" in meta["tool"]["poetry"]:
                description["title"] = meta["tool"]["poetry"]["name"].strip()
                logger.opt(colors=True).debug(
                    f"found name in poetry.toml <u>{description['title']}</u>"
                )
            if "description" in meta["tool"]["poetry"]:
                description["subtitle"] = meta["tool"]["poetry"]["description"].strip()
                logger.opt(colors=True).debug(
                    f"found description in poetry.toml <u>{description['subtitle']}</u>"
                )
    return description


def get_description_from_readmeRst(filestream) -> str:
    rx = re.compile(r"([\S])\1{3,}")
    lastline = ""
    while 1:
        line = filestream.readline().strip()
        if rx.match(line):
            logger.opt(colors=True).debug(
                f"found title line in readme.rst <u>{lastline}</u>"
            )
            return {"title": lastline}
        lastline = line


def get_description_from_poetsJson(string):
    o = json.loads(string)
    d = {}
    if "title" in o:
        d["title"] = o["title"]
    if "subtitle" in o:
        d["subtitle"] = o["subtitle"]
    return d


def join_title_and_subtitle(title: str, subtitle: str, ansi: bool) -> str:
    final_description = ""
    if title:
        if ansi:
            final_description += click.style(title, bold=True, underline=True)
        else:
            final_description += title

    if subtitle:
        if len(subtitle) > 82:
            subtitle = subtitle[:82] + "..."
        if final_description:
            final_description += " - " + subtitle
        else:
            final_description += subtitle
    return final_description


def get_dir_info(path: str) -> (str, str):
    """Get description of dir"""
    p = os.listdir(path)
    descriptions = {}
    for i in p:
        logger.trace(f"reading {i}")
        if i.lower() == "readme.md":
            descriptions[SOURCE_README_MD] = get_description_from_readmeMd(
                file_to_string(os.path.join(path, i))
            )
        elif i.lower() == "package.json":
            descriptions[SOURCE_PACKAGE_JSON] = get_description_from_packageJson(
                file_to_string(os.path.join(path, i))
            )
        elif i.lower() == "pyproject.toml":
            descriptions[SOURCE_PROJECT_TOML] = get_description_from_pyprojectToml(
                file_to_string(os.path.join(path, i))
            )
        elif i.lower() == "readme.rst":
            with open(os.path.join(path, i)) as f:
                descriptions[SOURCE_README_RST] = get_description_from_readmeRst(f)
        elif i.lower() == ".poets.json":
            descriptions[SOURCE_POETS_JSON] = get_description_from_poetsJson(
                file_to_string(os.path.join(path, i))
            )

    title = ""
    subtitle = ""
    for source in DESCRIPTION_SOURCE_PRIORITY:
        if source in descriptions:
            if "title" in descriptions[source]:
                if descriptions[source]["title"]:
                    logger.debug(f"using {source} for title")
                    title = descriptions[source]["title"]
                    break
    for source in DESCRIPTION_SOURCE_PRIORITY:
        if source in descriptions:
            if "subtitle" in descriptions[source]:
                if descriptions[source]["subtitle"]:
                    logger.debug(f"using {source} for subtitle")
                    subtitle = descriptions[source]["subtitle"]
                    break
    # if SOURCE_PACKAGE_JSON in descriptions:
    #     return join_title_and_subtitle(descriptions[SOURCE_PACKAGE_JSON])
    # elif SOURCE_PROJECT_TOML in descriptions:
    #     return join_title_and_subtitle(descriptions[SOURCE_PROJECT_TOML])
    # elif SOURCE_READ_ME in descriptions:
    #     return join_title_and_subtitle(descriptions[SOURCE_READ_ME])

    return title, subtitle


def thread_worker(q: Queue, path, u, f=None):
    while 1:
        a = q.get()
        logger.info(f"getting info for {a}")
        u[a + "/"] = get_dir_info(os.path.join(path, a))
        logger.info(f'info: {u[a+"/"]}')
        q.task_done()
        if f:
            f.update(1)


def loop_dirs(dirs, path, thread, f=None):
    u = {}
    if thread and thread > 0:
        q = Queue()
        for p in dirs:
            q.put(p)
        threads = []
        for _ in range(thread):
            worker = threading.Thread(target=thread_worker, args=(q, path, u, f),daemon=True)
            worker.start()
            threads.append(worker)
        q.join()
    else:
        for a in dirs:
            logger.info(f"getting info for {a}")
            u[a + "/"] = get_dir_info(os.path.join(path, a))
            logger.info(f'info: {u[a+"/"]}')
    return u


# @logger.catch
@click.command(
    help="A cli app to show directories with description. Works best with documented directories.",
    add_help_option=False,
)
@click.argument("path", type=click.Path(exists=True, readable=True), default=".")
@click.option("--ansi/--no-ansi", default=True, help="Disable ansi colored output")
@click.option("--dry", "-D", default=False, is_flag=True, help="Gide final stdout")
@click.option("--progress/--no-progress", default=True, help="Disable progress bar")
@click.option("-v", "--verbose", count=True, help="Set logging level, repeat for more")
@click.option(
    "-x", "--thread", type=int, default=0, help="Number of threads, 0 to disable"
)
@click.help_option("--help", "-h")
def main(ansi: bool, verbose: int, dry: bool, progress: bool, path: str, thread: int):
    if verbose > len(LOGGING_LEVELS):
        verbose = len(LOGGING_LEVELS)
    logger_config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": "<green>{time:HH:mm:ss.SSS}</green> - <lvl>{level}</lvl>: {message}",
                "level": LOGGING_LEVELS[verbose],
            },
        ],
    }
    logger.configure(**logger_config)
    logger.info(f"ansi status: {ansi}")

    logger.info(f"path: {path}")
    dirs = [o for o in os.listdir(path) if os.path.isdir(os.path.join(path, o))]

    if progress and not dry:
        if thread:
            with click.progressbar(length=len(dirs), label="Parsing directories") as f:
                u = loop_dirs(dirs, path, thread, f)
        else:
            with click.progressbar(dirs, label="Parsing directories") as di:
                u = loop_dirs(di, path, thread)
    else:
        u = loop_dirs(dirs, path, thread)

    if not dry:
        for l in sorted(u):
            if len(u[l]) >= 1:
                if ansi:
                    o = (
                        click.style(l, fg="blue")
                        + " "
                        + join_title_and_subtitle(*u[l], ansi=ansi)
                    )
                else:
                    o = l + " " + join_title_and_subtitle(*u[l], ansi=ansi)
            else:
                if ansi:
                    o = click.style(l, fg="blue")
                else:
                    o = l
            click.echo(o)


if __name__ == "__main__":
    main()
