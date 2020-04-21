import re

rep_re = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")

file_1 = open(r"C:\Users\ACER\PycharmProjects\zad1\Join_folder\join_file.txt", "r")
file_2 = open(r"C:\Users\ACER\PycharmProjects\zad1\Join_folder\join_file2.txt", "w+")
working_text = file_1.read()
matches = rep_re.findall(working_text)
for word in matches:
    choice = input(f"Input a/an {word}:")
    working_text = rep_re.sub(choice, working_text, 1)

file_2.write(working_text)
print(working_text)
file_1.close()
file_2.close()
