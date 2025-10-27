
import os

def get_extensions():
    path = input("Enter path: ")
    if not os.path.isdir(path):
        raise Exception
    extensions = set()
    for file in os.listdir(path):
        if not os.path.isfile(os.path.join(path, file)):
            continue
        extensions.add(file.split(".")[-1])
    print(sorted(extensions))

try:
    get_extensions()
except:
    print("Invalid path")