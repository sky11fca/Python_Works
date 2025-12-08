# Python script that computes the size of all files given a directory

import os, sys
from argparse import ArgumentError

try:
    if len(sys.argv) != 2:
        raise ArgumentError
    path = sys.argv[1]
    if not os.path.isdir(path):
        raise FileNotFoundError

    file_size = 0
    file_list = os.listdir(path)

    for root, dir, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size += os.path.getsize(file_path)
            except OSError:
                raise OSError

    print(f"Total size: {file_size} bytes")

except(FileNotFoundError, ArgumentError, OSError) as e:
    print(e)