# function that given a director path as parameter, will return a list of unique extensions in alphabetical order
import os

def get_extensions(path):
    extensions = set()
    for file in os.listdir(path):
        if not os.path.isfile(os.path.join(path, file)):
            continue
        extensions.add(file.split(".")[-1])
    return sorted(extensions)

print(get_extensions("/home/mrbogdanovich/Documents"))