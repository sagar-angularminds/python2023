import os
# from tkinter import filedialog as fd

# from dotenv import load_dotenv

from fileop import copy_file, append_file, display_file,print_directory

# load_dotenv()

# print(os.getenv("ENV_ID"))


def menu(i):
    switcher = {1: "append", 2: "copy", 3: "select", 4: "display", 5: "play", 6:"print_directory", 7: "exit"}
    return switcher.get(i, "Invalid input value")


m = ""

while m != "exit":
    i = input(
        """
     1. append 
     2. copy + separate directory
     3. select
     4. display
     5. play song
     6. print directory
     7. exit
     Enter your choice:"""
    )

    m = menu(int(i))

    if m == "append":
        input_file = input("Enter file name:")

        input_text = input("Enter text:")

        append_file(input_file, input_text)

    elif m == "copy":
        # open a file
        sample_file = open("./sample.txt", "r")

        copy_file(sample_file)

        # close the file
        sample_file.close()

    elif m == "select":
        # filename = fd.askopenfilename()
        # print(filename.split("/")[-1])
        print(m)

    elif m == "display":
        # filename = fd.askopenfilename()
        # display_file(filename)
        print(m)

    elif m == "play":
        # filename = fd.askopenfilename()
        print(m)

    elif m == "print_directory":
        # print_directory(os.getcwd())
        print(m)

    elif m == "exit":
        exit()

    else:
        print(m)
