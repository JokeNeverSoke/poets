from poets import get_dir_info

EXAMPLE_README_MD = r"""
# PoetsPy

A great python `ls` alternative

[Some Random Link](https://github.com)
"""

# example readme.rst from pingtop
# <https://github.com/laixintao/pingtop>
EXAMPLE_README_RST = r"""
pingtop 
=======

|CircleCI|

Ping multiple servers and show the result in a top like terminal UI.

|asciicast|

Install
-------

::

   pip install pingtop

Usage
-----

Then ping mutiple server:

::

   pingtop baidu.com google.com twitter.com

This project is using
`click <https://click.palletsprojects.com/en/7.x/>`__. Check help info
with ``pingtop -h``.

::

   ~ pingtop --help
   Usage: pingtop [OPTIONS] [HOST]...

   Options:
     -s, --packetsize INTEGER        specify the number of data bytes to be sent.
                                     The default is 56, which translates into 64
                                     ICMP data bytes when combined with the 8
                                     bytes of ICMP header data.  This option
                                     cannot be used with ping sweeps.  [default:
                                     56]
     -l, --logto PATH
     -v, --log-level [DEBUG|INFO|WARNING|ERROR|CRITICAL]
     --help                          Show this message and exit.

Why do I get ``Permission denied`` ?
------------------------------------

We use ICMP socket to send ping packet without ``sudo`` (See `this
post <https://blog.lilydjwg.me/2013/10/29/non-privileged-icmp-ping.41390.html>`__
by lilydjwg(in Chinese)), however, who(which group) can use this feature
is controled by a kernel parameter: ``net.ipv4.ping_group_range``.

::

   cat /proc/sys/net/ipv4/ping_group_range

   1    0

The default value is ``1 0``, this means the whose group number from 1
to 0 can use this feature(which means nobody can use this), so you get a
Permission denied .

To fix this, change this variable to a proper range include your group
id, like this:

::

   [vagrant@centos7 pingtop]$ id
   uid=1000(vagrant) gid=1000(vagrant) groups=1000(vagrant) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

   [vagrant@centos7 pingtop]$ sudo sysctl -w net.ipv4.ping_group_range='0 1001'
   net.ipv4.ping_group_range = 0 1001

Credits
-------

-  For the credits of ping.py’s implementation please refer
   `ping.py <./ping.py>`__.
-  The UI was built on `panwid <https://github.com/tonycpsu/panwid>`__
   thanks to @tonycpsu.
-  @\ `gzxultra <https://github.com/gzxultra>`__ helped to solve the
   permission issues.

.. |CircleCI| image:: https://circleci.com/gh/laixintao/pingtop.svg?style=svg
   :target: https://circleci.com/gh/laixintao/pingtop
.. |asciicast| image:: https://asciinema.org/a/onbBCmHzhltau7iqButUGx6yu.svg
   :target: https://asciinema.org/a/onbBCmHzhltau7iqButUGx6yu
"""

EXAMPLE_PYPROJECT_TOML = """
[build-system]
requires = [ "poetry>=0.12",]
build-backend = "poetry.masonry.api"

[tool.poetry]
name = "poetspy"
version = "0.1.0-alpha.2"
description = "A small cli util to show project directories"
readme = "README.MD"
homepage = "https://github.com/jokeneversoke/poets"
authors = [ "JokeNeverSoke <zengjoseph@hotmail.com>",]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.7"
marko = "^1.0.1"
click = "^7.1.2"
toml = "^0.10.2"

[tool.poetry.dev-dependencies]
black = "^20.8b1"
pytest = "^6.2.2"

[tool.poetry.scripts]
pt = "poetspy.poets:main"
"""

# package.json example from h5ai <https://larsjung.de/h5ai/>
EXAMPLE_PACKAGE_JSON = """\
{
  "name": "h5ai",
  "version": "0.29.2",
  "description": "Modern HTTP web server index.",
  "homepage": "https://larsjung.de/h5ai/",
  "bugs": "https://github.com/lrsjng/h5ai/issues",
  "author": "Lars Jung <lrsjng@gmail.com> (https://larsjung.de)",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/lrsjng/h5ai.git"
  },
  "scripts": {
    "lint": "eslint .",
    "test": "node test",
    "build": "node ghu release",
    "precommit": "npm run -s lint && npm run -s test"
  },
  "devDependencies": {
    "@babel/core": "7.8.7",
    "@babel/preset-env": "7.8.7",
    "eslint": "6.8.0",
    "ghu": "0.25.0",
    "jsdom": "16.2.0",
    "kjua": "0.6.0",
    "lolight": "1.3.0",
    "marked": "0.8.0",
    "normalize.css": "8.0.1",
    "null-loader": "3.0.0",
    "scar": "2.2.0"
  },
  "engines": {
    "node": ">=10.0.0"
  }
}
"""


def test_readme_md(tmpdir):
    readmeMd = tmpdir.join("README.MD")
    readmeMd.write(EXAMPLE_README_MD)
    assert get_dir_info(str(tmpdir)) == ("PoetsPy", "A great python ls alternative")


def test_pyproject_toml(tmpdir):
    pyprojectToml = tmpdir.join("pyproject.toml")
    pyprojectToml.write(EXAMPLE_PYPROJECT_TOML)
    assert get_dir_info(str(tmpdir)) == (
        "poetspy",
        "A small cli util to show project directories",
    )


def test_package_json(tmpdir):
    packageJson = tmpdir.join("package.json")
    packageJson.write(EXAMPLE_PACKAGE_JSON)
    assert get_dir_info(str(tmpdir)) == ("h5ai", "Modern HTTP web server index.")


def test_readme_rst(tmpdir):
    readmeRst = tmpdir.join("README.rst")
    readmeRst.write(EXAMPLE_README_RST)
    assert get_dir_info(str(tmpdir)) == ("pingtop", "")
