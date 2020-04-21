def concatenate(*args):
    result = ""
    for arg in args:
        result = result + str(arg) + ", "
    stripped = result.strip()
    result_without_last_char = stripped[:-1]
    return print(result_without_last_char)

concatenate(5, 6, "d")
