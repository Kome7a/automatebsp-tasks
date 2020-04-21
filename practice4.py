import re, os
search_exp = input("Type an expression you'd like to search for:")
expression = re.compile(rf"{search_exp}")

path = r"C:\Users\ACER\PycharmProjects\zad1\Join_folder"
for filename in os.listdir(path):
    with open(os.path.join(path, filename), "r") as f:
        print(expression.findall(f.read()))

