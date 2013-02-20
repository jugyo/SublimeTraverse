Traverse
========

Sublime Text 2 plugin to traverse directories and open file.

## Installation

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
$ git clone https://github.com/jugyo/SublimeTraverse.git Traverse
```

## Usage

The default deymap:

```json
[
  { "keys": ["super+shift+t", "super+shift+r"], "command": "traverse", "args": {"start": "root"} },
  { "keys": ["super+shift+t", "super+shift+h"], "command": "traverse", "args": {"start": "home"} },
  { "keys": ["super+shift+t", "super+shift+p"], "command": "traverse", "args": {"start": "project"} }
]
```
