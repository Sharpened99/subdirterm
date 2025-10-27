#!/bin/env python3

import os
import sys
import argparse


# Functions
def run_in_subdirectories(command: str, abs_path: bool | str) -> None:
    """
    Runs command in subdirectories found under abs_path if abs_path option is
    used. Otherwise, uses current working directory as starting point
    :param command: command to run
    :param abs_path: the absolute path to the starting point
            if abs_path option is used
    """
    if abs_path:
        os.chdir(abs_path)

    # Get working directory
    cwd: str = os.getcwd()

    # Get list of subdirectories
    subdirectories: list[str] = [d for d in os.listdir() if
                                 os.path.isdir(os.path.join(cwd, d))]

    print("Running " + command + " from following directories:")
    print(subdirectories)
    # Loop
    for subdir in subdirectories:
        print("")
        print(subdir + ":\n")

        os.chdir(os.path.join(cwd, subdir))
        os.system(command)


def run_file_iter(command_from_args: str, path_file: str, abs_path: bool | str) -> None:
    """
    Runs the command while replacing "§s" with a line from
    the file pointed to by path_file.
    :param command_from_args: the command to run
    :param path_file: path to the file with the replacement pattern
    :param abs_path: If the abs_path option is used, first navigates to the path
            pointed to by abs_path. Otherwise, use current working directory.
    """
    if abs_path:
        os.chdir(abs_path)

    file = open(path_file)
    file_lines: list[str] = file.read().split("\n")

    if file_lines[-1] == "":
        file_lines.pop()

    print("Running iterations from file\n")
    print(file_lines)
    for line in file_lines:
        print("")
        run_cmd = command_from_args.replace("§s", line)
        print("Running: ", run_cmd)
        os.system(run_cmd)


def parse_args() -> argparse.Namespace:
    """
    parse args given from CLI
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--abs", default=False, type=str,
        help="Use absolute path for starting directory. Uses current working "
             "directory otherwise."
    )
    parser.add_argument(
        "--file", default=False, type=str,
        help="Read list of strings from file and iterate through them. "
             "Replaces '§s' in the command with line in file"
    )
    parser.add_argument(
        "cmd", default="", type=str, nargs="+",
        help="The command to run. Put the command in quotes to avoid args "
             "like -a being interpreted as arguments for subdirterm."
    )

    return parser.parse_args()


def main(args: argparse.Namespace):
    cmd_start_index: int = 1
    # Options ---------------------------------------------

    # Absolute path
    if args.abs:
        print("Absolute path is:", args.abs)
    # File iteration
    if args.file:
        print("file name:", args.file)

    # Execution

    command_from_args = " ".join(args.cmd)

    if args.file:
        run_file_iter(command_from_args, args.file, args.abs)
    else:
        run_in_subdirectories(command_from_args, args.abs)

    print("\nDone\n")


if __name__ == "__main__":
    parsed_args = parse_args()
    main(parsed_args)
