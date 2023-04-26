import os
import sys


# Functions
def is_opt_abs(args: list[str]) -> (bool, str):
    opt_abs: bool = args[1].startswith("-") and args[1].__contains__("a")
    abs_path: str = ""
    if opt_abs:
        abs_path: str = ""
        for word in args[2:]:
            if word.startswith("path="):
                abs_path: str = word.partition("=")[2]
                break
    return opt_abs, abs_path


def is_opt_file_iter(args: list[str]) -> (bool, str):
    opt_file_iter: bool = args[1].startswith("-") and args[1].__contains__("f")
    path_file: str = ""
    if opt_file_iter:
        path_file: str = ""
        for word in args[2:]:
            if word.startswith("file="):
                path_file = word.partition("=")[2]
                break
    return opt_file_iter, path_file


def run_in_subdirectories(command: str, abs1: bool, abs_path: str):
    if abs1:
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


def run_file_iter(command_from_args: str, path_file: str, abs1: str, abs_path: str):
    if abs1:
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


def main():
    # Get args ------------------------------------------------

    args: list[str] = sys.argv
    cmd_start_index: int = 1

    if len(args) < 2:
        print("Incorrect number of arguments: must be at least 2")
        exit(1)

    # Options ---------------------------------------------

    # Absolute path
    opt_abs, abs_path = is_opt_abs(args)

    # File iteration
    opt_file_iter, file = is_opt_file_iter(args)

    # Index adjustment
    if opt_abs or opt_file_iter:
        cmd_start_index += 2
        if opt_abs and opt_file_iter:
            cmd_start_index += 1

    # Execution

    command_from_args = " ".join(args[cmd_start_index:])

    if opt_file_iter:
        run_file_iter(command_from_args, file, opt_abs, abs_path)
    else:
        run_in_subdirectories(command_from_args, opt_abs, abs_path)

    print("\nDone")


if __name__ == "__main__":
    main()
