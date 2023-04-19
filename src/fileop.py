import os
import shutil


# create a separate directory for each name and save the name in respective folder
def copy_file(file_content):
    for line in file_content:
        try:
            folder_name = line.split()[0]
            if not len(folder_name):
                continue
        except:
            print("Empty line found")

        path = os.path.join(os.getcwd() + "/output", folder_name)

        # check if directory already exist then first remove it and create new with the same name
        if os.path.exists(path) and os.path.isdir(path):
            shutil.rmtree(path)
            os.makedirs(path)
        else:
            os.makedirs(path)

        try:
            name = open(path + "/" + folder_name + ".txt", "w")
            name.write(line)
        except:
            print("Exception occured while writting the file")


# append input text at the end of given file
def append_file(file_name, input_text):
    path = os.path.join(os.getcwd() + "/", file_name)

    input_file = open(path, "a+")

    input_file.write(input_text + "\n")

    input_file.close()


# display content of the given file
def display_file(file_name):
    file = open(file_name)
    print(file)

# walk through given directory and print(dirpath,dirnames,filenames)
def print_directory(directory):
    files = os.walk(directory)
    for x in files:
        print(x)
