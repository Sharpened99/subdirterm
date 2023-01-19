import os
import sys


# Get args
args = sys.argv

# Options
optAbs = args[1] == "-abs"
## Absolute path
if optAbs:
    os.chdir(args[2])

# Get command
command = " ".join(args[3 if optAbs else 1:])

# Get working directory
cwd = os.getcwd()

# Get list of subdirectories
subdirectories = [d for d in os.listdir() if 
    os.path.isdir(os.path.join(cwd, d))]

print("Running " + command + " from following directories:")
print(subdirectories)

# Loop
for subdir in subdirectories:
    print("\n\n")
    print(subdir + ":\n")

    os.chdir(os.path.join(cwd, subdir))
    os.system(command)

print("\n\nDone")
