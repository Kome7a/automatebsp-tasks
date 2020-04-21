#! python3
# renameDates.py - Renames files with American date format MM:DD:YYYY to European date formats DD:MM:YYYY

import shutil, os, re

# Create regex to match American date format

date_pattern = re.compile(r"""
^(.*?)              #all text before date
([01]?\d)-         #one or two digits for month
([0-3]?\d)-     #one or two digits for day
((19|20)\d\d)-       #four digits for the year
(.*?)$              #all text after date                              
""", re.VERBOSE)

# Loop over the files in the working directory.
for amer_Filename in os.listdir("."):
    mo = date_pattern.search(amer_Filename)

    # Skip files without a date
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the european style name.
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

    # Get the full absolute paths.
    absWorkingDir = os.path.abspath(".")
    amer_Filename = os.path.join(absWorkingDir, amer_Filename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the filename.
    print(f"Renaming {amer_Filename} to {euroFilename}.")
    #shutil.move(amer_Filename, euroFilename)