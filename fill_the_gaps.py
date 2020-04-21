import re, os, shutil

file_search = re.compile(r"(capitalsquiz)(\d+)(\.txt)")
folder_name = os.path.abspath("Text_folder")
files = os.listdir(folder_name)


def sort_by_idx(file_name):
    match = file_search.search(file_name)
    return int(match.group(2))


files_to_change = filter(lambda s: "answers" not in s, files)
sorted_files = sorted(files_to_change, key=sort_by_idx)

idx = 0
for filename in sorted_files:
    mo = file_search.search(filename)
    idx = idx + 1
    file_num = int(mo.group(2))

    if file_num + 1 != idx:
        new_name = mo.group(1) + str(idx) + mo.group(3)
        shutil.move(folder_name + f"\\{filename}", folder_name + f"\\{new_name}")
