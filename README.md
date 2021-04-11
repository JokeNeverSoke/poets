# Poets

[![License](https://img.shields.io/github/license/jokeneversoke/poets)](https://github.com/JokeNeverSoke/poets/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/poetspy)](https://pypi.org/project/poetspy/)
[![Build Status](https://travis-ci.com/JokeNeverSoke/poets.svg?branch=master)](https://travis-ci.com/JokeNeverSoke/poets)
[![Coverage Status](https://coveralls.io/repos/github/JokeNeverSoke/poets/badge.svg?branch=master)](https://coveralls.io/github/JokeNeverSoke/poets?branch=master)
[![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/PyPI/poetspy)](https://libraries.io/pypi/poetspy)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/poetspy)](https://pypi.org/project/poetspy/)

A small script that goes over the directories of the current directories, and print them
`ls`-like, but also showing descriptions scraped to the best of the script's abilities

![demonstration](https://raw.githubusercontent.com/JokeNeverSoke/poets/master/assets/demonstration.gif)


## Getting Started

Installation with pip

```bash
$ pip install poetspy
```

Installation with pipx

```bash
$ pipx install poetspy
```

## Usage

### Basic

```bash
$ cd projects  # cd into my main project dir
$ pt  # show my projects w/ descriptions
deno/
study/ study - This project was bootstrapped with Create React App.
hanasu/ hanasu
ipfs/
randomcodes/ randomcodes - Some personal random codes
susume/ susume - This template should help get you started developing with Vue 3 and Typescript in ...
hns/ hns - UsageCommands
study-backend/ node-js-getting-started - A sample Node.js app using Express
BVG/ bvg - Generates a bad video from a noun and a verb
logic/ logic
poetspy/ poetspy - A small cli util to show project directories
randomlogging/ My logging xps - blah blah blah, no one wants to write READMEs
blog/ jokens-blog - A starter for a blog powered by Gatsby and Markdown
call/
itermtests/
workflow/
jns/ jns - Some random css
htmldesktop/
modules/
vapi/ tmp - yarn install
```

### Custom Title & Descriptions

```bash
$ cd project/
$ ptg title Hello World Project  # set cwd title
title set to Hello World Project
$ ptg des Python Tutorial  # set cwd description
description set to Python Tutoria
```
