# subdirterm

## What is this?

subdirterm is a script allowing you to quickly execute terminal commands 
in subdirectories from a starting directory

## Usage
```
subdirterm.py [-h] [--abs ABS] [--file FILE] cmd [cmd ...]
```

## Options
### Absoulute path
If the option `--abs` is used, `ABS` denotes the absolute path to the starting directory the script will be executing from.
If this option is not present, the starting directory is the current working directory.

### File iteration
If the option `--file` is used, the script will iterate through the lines of the file named by `FILE` and replace `§s` in the command with the current line.

## Prerequisites

- Python 3
