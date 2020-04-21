import os
# ("C:\\Users\ACER\PycharmProjects\zad1\Join_folder\join_file.txt)
os.chdir("Join_folder")
with open("join_file.txt", "r") as file:
    copy = file.read()

with open("join_file2.txt", "r+") as file:
    file.write(f"\n{copy}")

with open("join_file2.txt", "r") as file:
    print(file.read())

