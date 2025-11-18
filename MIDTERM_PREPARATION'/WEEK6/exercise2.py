# Given a path, rename all files from the respective to add a sequential nr prefix
# e.g. 1.txt, 2.txt, 3.txt, etc.
# handle errors: Directory doesn't exist, file cannot be renamed

import os
import sys
from argparse import ArgumentError


def rename_files(path):
    file_list = os.listdir(path)
    for index, file_name in enumerate(file_list):
        os.rename(os.path.join(path, file_name), os.path.join(path, f"{index+1}.txt"))

try:
    if len(sys.argv) != 2:
        raise ArgumentError
    path = sys.argv[1]
    if not os.path.isdir(path):
        raise FileNotFoundError

    rename_files(path)
except (FileNotFoundError, ArgumentError) as e:
    print(e)
except:
    print("Error reading the file")