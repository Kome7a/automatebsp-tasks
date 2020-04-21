def upper_lower(string):
    n = 0
    i = 0
    result_upper = 0
    result_lower = 0
    for letter in string:
        if letter.islower():
            n = n + 1
            result_lower = n
        if letter.isupper():
            i = i + 1
            result_upper = i
    print("No of upper case characters: " + str(result_upper),
          "\nNo of lower case characters: " + str(result_lower))


upper_lower("Python is Very Cool Language")
