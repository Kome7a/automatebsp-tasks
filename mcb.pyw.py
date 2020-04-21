#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mbcShelf = shelve.open("mcb")

# Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mbcShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == "del":
    mbcShelf.pop(sys.argv[2])
if len(sys.argv) == 2:
    if sys.argv[1].lower == "list":
        pyperclip.copy("".join(list(mbcShelf.keys())))
    elif sys.argv[1].lower() == "del":
        mbcShelf.clear()
    elif sys.argv[1] in mbcShelf:
        pyperclip.copy(mbcShelf[sys.argv[1]])


mbcShelf.close()
