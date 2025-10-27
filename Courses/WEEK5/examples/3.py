# function that has as parameter a string my_path
# if the parameter is a file, will return the last 20 bytes that contains in the file
# if the parameter is a directory, will return a tuple list (extension, count) consisting of file extension and the number of appearances.
# the list should be sorted in descending order
# operation is recursive

import os

def get_file_content(my_path):
    if os.path.isfile(my_path):
        with open(my_path, "r") as f:
            return f.read()[-20:]
    elif os.path.isdir(my_path):
        result = {}
        for file in os.listdir(my_path):
            absolut_path = os.path.join(my_path, file)
            if os.path.isdir(absolut_path):
                get_file_content(os.path.join(my_path, file))
            result[file.split(".")[-1]] = result.get(file.split(".")[-1], 0) + 1
        return sorted(result.items(), key=lambda x: x[1], reverse=True)

print(get_file_content("/home/mrbogdanovich/Documents"))
print(get_file_content("1.py"))