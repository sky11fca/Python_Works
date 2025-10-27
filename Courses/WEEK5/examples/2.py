# function given a directory and a file,
# inside the file will be written all absolute paths for each line
# where the item begins with A

import os

def write_to_file(directory, file):
    with open(file, "w") as f:
        for file in os.listdir(directory):
            if file.startswith("A"):
                f.write(os.path.abspath(os.path.join(directory, file)) + "\n")
        f.close()


write_to_file("/home/mrbogdanovich/Documents", "A.txt")