import os
import csv

os.chdir("C://Users//ACER/Desktop/CSV")
os.makedirs("headerRemoved", exist_ok=True)

# Loop through every single file in the cwd.
for csv_filename in os.listdir("."):
    if not csv_filename.endswith(".csv"):
        continue    # skip not csv files.
    print("Removing Header from " + csv_filename + "...")

    csv_rows = []
    csv_file_obj = open(csv_filename)
    reader_object = csv.reader(csv_file_obj)
    for row in reader_object:
        if reader_object.line_num == 1:
            continue    # Skip first row.
        csv_rows.append(row)
    csv_file_obj.close()

    csv_file_obj = open(os.path.join("headerRemoved", csv_filename), "w", newline='')
    csv_writer = csv.writer(csv_file_obj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_obj.close()
