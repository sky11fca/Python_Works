# script that given a path will return a number of files with each exception


import os, sys

try:
    path = sys.argv[1]
    if not os.path.isdir(path):
        raise FileNotFoundError

    extension_dict = {}

    for root, dir, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                extension = file_path.split(".")[-1]
                if extension in extension_dict:
                    extension_dict[extension] += 1
                else:
                    extension_dict[extension] = 1
            except IndexError:
                continue

    print(extension_dict)
except (FileNotFoundError, IndexError) as e:
    print(e)