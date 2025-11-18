# given a path to a directory and a file
# on that said file, it will be writen all paths to files inside folder


import os, sys

if len(sys.argv) != 3:
    print("Usage: python3 exercise2.py <dir> <file_out>")
    sys.exit(1)

try:
    path = sys.argv[1]
    file_out = sys.argv[2]

    if not os.path.isdir(path):
        raise FileNotFoundError

    with open(file_out, "w") as f:
        for root, dir, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                f.write(f"{file_path}\n")
except FileNotFoundError:
    print(f"Directory {path} not found")