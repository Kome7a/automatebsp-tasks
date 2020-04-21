def concatenate_string(first_name="default", last_name="default", age=int()):
    if first_name and last_name and age:
        concat = str.join(" ", (first_name, last_name, str(age)))
        return concat
    else:
        return "Missing one or all arguments of the function!"


print(concatenate_string())
