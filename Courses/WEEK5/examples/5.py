# function that has as parameter target and to_search
# returns a list that has to_search inside
# if target is a file then will search inside of it.
# if is a directory then will search recursively inside of it
# if is something else entirely will throw a ValueError exception

import os

def list_of_grep(target, to_search):
    if os.path.isfile(target):
        with open(target, "r") as f:
            buff = f.read()
            if to_search in buff:
                return [buff]
            else:
                return []

    elif os.path.isdir(target):
        result = []
        for file in os.listdir(target):
            result.extend(list_of_grep(os.path.join(target, file), to_search))
        return result
    else:
        raise ValueError



try:
    print(list_of_grep(".", "Linux"))
except ValueError:
    print("Invalid path")