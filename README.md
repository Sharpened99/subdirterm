# subdirterm

## What is this?

subdirterm is a script allowing you to quickly execute terminal commands 
in subdirectories from a starting directory

## Usage
```
python3 subdirterm <command>
```

## Options
### Absoulute path
If the option `-a` is used, there must be an argument starting with `path=` giving an absolute path to the starting directory.
If this option is not present, the starting directory is the current working directory.

### File iteration
`-f` Iterates through the file given by the argument starting with `file=` and replaces `§s` in the command with a line in the file

## Prerequisites

- Python 3