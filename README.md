# subdirterm

## What is this?

subdirterm is a script allowing you to quickly execute terminal commands 
in subdirectories from a starting directory

## Usage
```
python3 subdirterm [-<options>] <command>
```

## Options
### Absoulute path
If the option `-a` is used, there must be an argument starting with `path=` giving an absolute path to the starting directory.
If this option is not present, the starting directory is the current working directory.

### File iteration
If the option `-f` is used, the script will run through the lines of the file pointed to by the argument starting with `file=` and replace `§s` with the current line

## Prerequisites

- Python 3
