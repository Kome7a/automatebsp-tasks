import re


def is_strong(password):
    check = re.compile(r'''
    (?=\D*\d)
    (?=[^A-Z]*[A-Z])
    (?=[^a-z]*[a-z])
    ^[a-zA-Z0-9_]{8,}$
    ''', re.VERBOSE)
    if check.search(password):
        print(f"Password '{password}' is strong.")
        return True
    else:
        print(f"Password '{password}' is NOT strong.")
        return False


my_pass = "K1ngs0fl30n"
ur_pass = "kon1"

is_strong(ur_pass)
is_strong(my_pass)
