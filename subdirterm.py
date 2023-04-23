import os
import sys


# Functions
def run_in_subdirectories():
    # Get working directory
    cwd = os.getcwd()

    # Get list of subdirectories
    subdirectories = [d for d in os.listdir() if
                      os.path.isdir(os.path.join(cwd, d))]

    print("Running " + command_from_args + " from following directories:")
    print(subdirectories)
    # Loop
    for subdir in subdirectories:
        print("\n\n")
        print(subdir + ":\n")

        os.chdir(os.path.join(cwd, subdir))
        os.system(command_from_args)


def run_file_iter():
    print("Running iterations from file\n")
    print(file_lines)
    for line in file_lines:
        print("\n")
        run_cmd = command_from_args.replace("§s", line)
        print("Running: ", run_cmd)
        os.system(run_cmd)


# Get args ------------------------------------------------

args: list[str] = sys.argv
cmd_start_index: int = 1

# Options ---------------------------------------------

# Absolute path
opt_abs = args[1].__contains__("a")
if opt_abs:
    abs_path: str = ""
    for word in args[2:]:
        if word.startswith("path="):
            abs_path = word.partition("=")[2]
            break
    os.chdir(abs_path)

# File iteration
opt_file_iter = args[1].__contains__("f")
if opt_file_iter:
    path_file: str = ""
    for word in args[2:]:
        if word.startswith("file="):
            path_file = word.partition("=")[2]
            break
    file = open(path_file)
    file_lines = file.read().split("\n")

if opt_abs or opt_file_iter:
    cmd_start_index += 2
    if opt_abs and opt_file_iter:
        cmd_start_index += 1

# Execution

# Get command
command_from_args = " ".join(args[cmd_start_index:])

if opt_file_iter:
    run_file_iter()
else:
    run_in_subdirectories()

print("\n\nDone")
