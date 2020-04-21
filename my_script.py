import os
directory = os.getcwd()
os.chdir(directory)
os.chdir("Join_folder")
with open("join_file2.txt", "w") as file:
    file.write("az""\naz")\

with open("join_file.txt", "r") as file:
    print(file.read())

