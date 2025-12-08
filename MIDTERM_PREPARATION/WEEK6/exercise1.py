# Given a path as an argument
# Will search for files that have the same extension (also given as an parameter)
# for each file with this extension, will print out it's contents
# Handle the coresponding errors: Invalid Path, Incorrect Extension, error reading the files

import sys, os
from argparse import ArgumentError

try:
    if len(sys.argv) != 3:
        raise ArgumentError

    path = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.isdir(path):
        raise FileNotFoundError



    for file in os.listdir(path):
        if file.endswith(extension):
            with open(os.path.join(path, file), 'r') as f:
                print(f.read())
                f.close()
except (FileNotFoundError, ArgumentError) as e:
    print(e)
except:
    print("Error reading the file")