#! python3
# regex_email_phonenumber.py --> Finds e-mails and phone numbers on the clipboard.

import pyperclip
import re


phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              #area code
(\s|-|\.)?                      #separator
(\d{3})                         #first 3 digits
(\s|-|\.)                       #separator
(\d{4})                         #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)''', re.VERBOSE)

email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+       #pattern
@                       #@
[a-zA-Z0-9.-]+          #domain name
(\.[a-zA-z]{2,4})       #dot-something
)''', re.VERBOSE)


# find matches

text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_num += " x" + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone or e-mail addresses found.')