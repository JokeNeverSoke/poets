EXAMPLE_README_MD1 = r"""
# PoetsPy

A great python `ls` alternative

[Some Random Link](https://github.com)
"""

EXAMPLE_README_MD2 = r"""
![image](source)
![anotherimage](and_source)

# Title

![alt img](alt_source)

this is just a random readme
"""

# Taken from <https://github.com/IgorAntun/node-chat>
EXAMPLE_README_MD3 = r"""
Node.JS Chat
============
[![GitHub Stars](https://img.shields.io/github/stars/IgorAntun/node-chat.svg)](https://github.com/IgorAntun/node-chat/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/IgorAntun/node-chat.svg)](https://github.com/IgorAntun/node-chat/issues) [![Current Version](https://img.shields.io/badge/version-1.0.7-green.svg)](https://github.com/IgorAntun/node-chat) [![Live Demo](https://img.shields.io/badge/demo-online-green.svg)](https://igorantun.com/chat) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/IgorAntun/node-chat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

This is a node.js chat application powered by SockJS and Express that provides the main functions you'd expect from a chat, such as emojis, private messages, an admin system, etc.

![Chat Preview](http://i.imgur.com/lgRe8z4.png)

---
## Buy me a coffee

Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<a href="https://www.buymeacoffee.com/igorantun" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

---

## Features
- Material Design
- Emoji support
- User @mentioning
- Private messaging
- Message deleting (for admins)
- Ability to kick/ban users (for admins)
- See other user's IPs (for admins)
- Other awesome features yet to be implemented

.
![User Features](http://i.imgur.com/WbF1fi2.png)

.
![Admin Features](http://i.imgur.com/xQFaadt.png)


#### There are 3 admin levels:
- **Helper:** Can delete chat messages
- **Moderator:** The above plus the ability to kick and ban users
- **Administrator:** All the above plus send global alerts and promote/demote users

---

## Setup
Clone this repo to your desktop and run `npm install` to install all the dependencies.

You might want to look into `config.json` to make change the port you want to use and set up a SSL certificate.

---

## Usage
After you clone this repo to your desktop, go to its root directory and run `npm install` to install its dependencies.

Once the dependencies are installed, you can run  `npm start` to start the application. You will then be able to access it at localhost:3000

To give yourself administrator permissions on the chat, you will have to type `/role [your-name]` in the app console.

---

## License
>You can check out the full license [here](https://github.com/IgorAntun/node-chat/blob/master/LICENSE)

This project is licensed under the terms of the **MIT** license.
"""

# taken from <https://github.com/athityakumar/colorls>
EXAMPLE_README_MD4 = r"""
# Color LS

[![forthebadge](http://forthebadge.com/images/badges/made-with-ruby.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

[![Gem Version](https://badge.fury.io/rb/colorls.svg)](https://badge.fury.io/rb/colorls)
[![Build Status](https://travis-ci.org/athityakumar/colorls.svg?branch=master)](https://travis-ci.org/athityakumar/colorls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields)](http://makeapullrequest.com)

A Ruby script that colorizes the `ls` output with color and icons. Here are the screenshots of working example on an iTerm2 terminal (Mac OS), `oh-my-zsh` with `powerlevel9k` theme and `powerline nerd-font + awesome-config` font with the `Solarized Dark` color theme.

 ![image](https://user-images.githubusercontent.com/17109060/32149040-04f3125c-bd25-11e7-8003-66fd29bc18d4.png)

*If you're interested in knowing the powerlevel9k configuration to get this prompt, have a look at [this gist](https://gist.github.com/athityakumar/1bd5e9e24cd2a1891565573a893993eb).*

# Table of contents

- [Usage](#usage)
  - [Flags](#flags)
    - `-1`
    - `-a`   (or) `--all`
    - `-A`   (or) `--almost-all`
    - `-d`   (or) `--dirs`
    - `-f`   (or) `--files`
    - `-h`   (or) `--help`
    - `-l`   (or) `--long`
    - `-r`   (or) `--report`
    - `--tree` (or) `--tree=[DEPTH]`
    - `--gs` (or) `--git-status`
    - `--sd` (or) `--sort-dirs` or `--group-directories-first`
    - `--sf` (or) `--sort-files`
    - `-t`
  - [Combination of flags](#combination-of-flags)
- [Installation](#installation)
- [Recommended configurations](#recommended-configurations)
- [Custom configurations](#custom-configurations)
- [Updating](#updating)
- [Uninstallation](#uninstallation)
- [Contributing](#contributing)
- [License](#license)

# Usage

[(Back to top)](#table-of-contents)

Man pages have been added. Checkout `man colorls`.

### Flags

- With `-1` : Lists one entry per line

  ![image](https://user-images.githubusercontent.com/17109060/32149062-4f0547ca-bd25-11e7-98b6-587467379704.png)

- With `-a` (or) `--all` : Does not ignore entries starting with '.'

  ![image](https://user-images.githubusercontent.com/17109060/32149045-182eb39e-bd25-11e7-83d4-897cb14bcff3.png)

- With `-A` (or) `--almost-all` : Does not ignore entries starting with '.', except `./` and `../`

  ![image](https://user-images.githubusercontent.com/17109060/32149046-1ef7664e-bd25-11e7-8bd9-bfc3c8b27b74.png)

- With `-d` (or) `--dirs` : Shows only directories

  ![image](https://user-images.githubusercontent.com/17109060/32149066-5f842aa8-bd25-11e7-9bf0-23313b717182.png)

- With `-f` (or) `--files` : Shows only files

  ![image](https://user-images.githubusercontent.com/17109060/32149065-5a27c9d4-bd25-11e7-9a2b-fd731d76a058.png)

- With `-h` (or) `--help` : Prints a very helpful help menu

  ![image](https://user-images.githubusercontent.com/17109060/32149096-cf2cf5b0-bd25-11e7-84b6-909d79099c98.png)

- With `-l` (or) `--long` : Shows in long listing format

  ![image](https://user-images.githubusercontent.com/17109060/32149049-2a63ae48-bd25-11e7-943c-5ceed25bd693.png)

- With `-r` (or) `--report` : Shows brief report about number of files and folders shown

  ![image](https://user-images.githubusercontent.com/17109060/32149082-96a83fec-bd25-11e7-9081-7f77e4c90e90.png)

- With `--tree` (or) `--tree=[DEPTH]` : Shows tree view of the directory with the specified depth (default 3)

  ![image](https://user-images.githubusercontent.com/17109060/32149051-32e596e4-bd25-11e7-93a9-5e50c8d2bb19.png)

- With `--gs` (or) `--git-status` : Shows git status for each entry

  ![image](https://user-images.githubusercontent.com/17109060/32149075-7a1a1954-bd25-11e7-964e-1adb173aa2b9.png)

- With `--sd` (or) `--sort-dirs` or `--group-directories-first` : Shows directories first, followed by files

  ![image](https://user-images.githubusercontent.com/17109060/32149068-65117fc0-bd25-11e7-8ada-0b055603e3fd.png)

- With `--sf` (or) `--sort-files` : Shows files first, followed by directories

  ![image](https://user-images.githubusercontent.com/17109060/32149071-6b379de4-bd25-11e7-8764-a0c577e526a1.png)

- With `-t` : Sort by modification time, newest first (NEED TO ADD IMAGE)

- With color options : `--light` or `--dark` can be passed as a flag, to choose the appropriate color scheme. By default, the dark color scheme is chosen. In order to tweak any color, read [Custom configurations](#custom-configurations).

### Combination of flags

- Using `--gs` with `-t` :

  ![image](https://user-images.githubusercontent.com/17109060/32149076-8423c864-bd25-11e7-816e-8642643d2c27.png)

- Using `--gs` with `-l` :

  ![image](https://user-images.githubusercontent.com/17109060/32149078-899b0622-bd25-11e7-9810-d398eaa77e32.png)

- Using `--sd` with `-l` and `-A` :

  ![image](https://user-images.githubusercontent.com/17109060/32149084-9eb2a416-bd25-11e7-8fb7-a9d336c6e038.png)

# Installation

[(Back to top)](#table-of-contents)

1. Install Ruby (preferably, version >= 2.5)
2. Install the patched fonts of powerline nerd-font and/or font-awesome. Have a look at the [Nerd Font README](https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md) for more installation instructions.

    *Note for `iTerm2` users - Please enable the Nerd Font at iTerm2 > Preferences > Profiles > Text > Non-ASCII font > Hack Regular Nerd Font Complete.*

    *Note for `HyperJS` users - Please add `"Hack Nerd Font"` Font as an option to `fontFamily` in your `~/.hyper.js` file.*

3. Install the [colorls](https://rubygems.org/gems/colorls/) ruby gem with `gem install colorls`

    *Note for `rbenv` users - In case of load error when using `lc`, please try the below patch.*

    ```sh
    rbenv rehash
    rehash
    ```

4. Enable tab completion for flags by entering following line to your shell configuration file (`~/.bashrc` or `~/.zshrc`) :
    ```bash
    source $(dirname $(gem which colorls))/tab_complete.sh
    ```

5. Start using `colorls` :tada:

6. Have a look at [Recommended configurations](#recommended-configurations) and [Custom configurations](#custom-configurations).

# Recommended configurations

[(Back to top)](#table-of-contents)

1. To add some short command (say, `lc`) with some flag options (say, `-l`, `-A`, `--sd`) by default, add this to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.) :
    ```sh
    alias lc='colorls -lA --sd'
    ```

2. For changing the icon(s) to other unicode icons of choice (select icons from [here](https://nerdfonts.com/)), change the YAML files in a text editor of your choice (say, `subl`)

    ```sh
    subl $(dirname $(gem which colorls))/yaml
    ```

# Custom configurations

[(Back to top)](#table-of-contents)

You can overwrite the existing icons and colors mapping by copying the yaml files from `$(dirname $(gem which colorls))/yaml` into `~/.config/colorls`, and changing them.

- To overwrite color mapping :

  Please have a look at the [list of supported color names](https://github.com/sickill/rainbow#color-list). You may also use a color hex code as long as it is quoted within the YAML file and prefaced with a `#` symbol.

  Let's say that you're using the dark color scheme and would like to change the color of untracked file (`??`) in the `--git-status` flag to yellow. Copy the defaut `dark_colors.yaml` and change it.

  ```sh
  cp $(dirname $(gem which colorls))/yaml/dark_colors.yaml ~/.config/colorls/dark_colors.yaml`
  ```

  In the `~/.config/colorls/dark_colors.yaml` file, change the color set for `untracked` from `darkorange` to `yellow`, and save the change.

  ```
  untracked: yellow
  ```

  Or, using hex color codes:

  ```
  untracked: '#FFFF00'
  ```

- To overwrite icon mapping :

  Please have a look at the [list of supported icons](https://nerdfonts.com/). Let's say you want to add an icon for swift files. Copy the default `files.yaml` and change it.

  ```sh
  cp $(dirname $(gem which colorls))/yaml/files.yaml ~/.config/colorls/files.yaml`
  ```

  In the `~/.config/colorls/files.yaml` file, add a new icon / change an existing icon, and save the change.


  ```
  swift: "\uF179"
  ```

- User contributed alias configurations :

  - [@rjhilgefort](https://gist.github.com/rjhilgefort/51ea47dd91bcd90cd6d9b3b199188c16)


# Updating

[(Back to top)](#table-of-contents)

Want to update to the latest version of `colorls`?

```sh
gem update colorls
```

# Uninstallation

[(Back to top)](#table-of-contents)

Want to uninstall and revert back to the old style? No issues (sob). Please feel free to open an issue regarding how we can enhance `colorls`.

```sh
gem uninstall colorls
```

# Contributing

[(Back to top)](#table-of-contents)

Your contributions are always welcome! Please have a look at the [contribution guidelines](CONTRIBUTING.md) first. :tada:

# License

[(Back to top)](#table-of-contents)


The MIT License (MIT) 2017 - [Athitya Kumar](https://github.com/athityakumar/). Please have a look at the [LICENSE.md](LICENSE.md) for more details.

"""

# example readme.rst from pingtop
# <https://github.com/laixintao/pingtop>
EXAMPLE_README_RST1 = r"""
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

EXAMPLE_PYPROJECT_TOML1 = r"""
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
EXAMPLE_PACKAGE_JSON1 = r"""{
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
