# given a path as parameter

# if is a path to a file, it will return the last 20 chars
# if is a path to a directory, it will return a list of tuples (extension, count) in a decreasing order by count. Iterate the files recursively


import os, sys

if len(sys.argv) != 2:
    print("Usage: python3 exercise3.py <path>")
    sys.exit(1)

my_path = sys.argv[1]

try:
    if os.path.isfile(my_path):
        with open(my_path, "r") as f:
            print(f.read()[-20:])
    elif os.path.isdir(my_path):
        dir_dict = {}

        for root, dir, files in os.walk(my_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    extension = file_path.split(".")[-1]
                    if extension in dir_dict:
                        dir_dict[extension] += 1
                    else:
                        dir_dict[extension] = 1
                except IndexError:
                    continue

        print(sorted(dir_dict.items(), key=lambda x: x[1], reverse=True))
except FileNotFoundError:
    print(f"Directory {my_path} not found")