# Given a path to a directory, return a list of all file extension sorted alphabetically

import os, sys

path = sys.argv[1]

list_of_extension = []

for root, dir, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            extension = file_path.split(".")[-1]
            if extension not in list_of_extension:
                list_of_extension.append(extension)
        except IndexError:
            continue

print(sorted(list_of_extension))

