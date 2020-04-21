import os

path = r"C:\Users\ACER\Documents"
for foldernames, subfolders, filenames in os.walk(path):
    total_size = 0
    print(f"Folder {foldernames}")
    for filename in filenames:
        print(f"Filename : {filename}")
        path_to_file = os.path.join(foldernames, filename)
        print('path to file ', path_to_file)
        size = os.path.getsize(path_to_file)
        total_size = total_size + size
    print(f"{os.path.basename(foldernames)}", f"Size ({total_size})")



