#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, zipfile


def backup_to_zip(folder):

    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)

    # Figure out the name of the zip_file by checking if it already exists.
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number = number + 1

    # Create zip_file
    print(f"Creating {zip_file_name}...")
    backup_zip = zipfile.ZipFile(zip_file_name, "w")

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")

        # Add files in current folder to zip.
        backup_zip.write(foldername)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue  # don't backup the backup ZIP files
            backup_zip.write(os.path.join(foldername, filename))
        backup_zip.close()


backup_to_zip("Text_folder")
