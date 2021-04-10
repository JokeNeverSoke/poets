import json
import os
from pathlib import Path

import click


@click.command()
@click.argument("title", nargs=-1, required=True)
def title(title):
    t = " ".join(title)
    p = Path("./.poets.json")
    if p.exists():
        if p.is_dir():
            click.secho(".poets.json is a directory!", fg="red")
            return
        k = json.load(p.open())
        k["title"] = t
    else:
        k = {"title": t}
    json.dump(k, p.open("w"))
    click.echo(
        click.style("title set to", fg="blue")
        + " "
        + click.style(t, fg="blue", underline=True)
    )


@click.command()
@click.argument("des", nargs=-1, required=True)
def des(des):
    t = " ".join(des)
    p = Path("./.poets.json")
    if p.exists():
        if p.is_dir():
            click.secho(".poets.json is a directory!", fg="red")
            return
        k = json.load(p.open())
        k["subtitle"] = t
    else:
        k = {"subtitle": t}
    json.dump(k, p.open("w"))
    click.echo(
        click.style("description set to", fg="blue")
        + " "
        + click.style(t, fg="blue", underline=True)
    )


@click.group()
def main():
    pass


main.add_command(title)
main.add_command(des)

if __name__ == "__main__":
    main()
