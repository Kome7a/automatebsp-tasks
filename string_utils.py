def format_string(string: str, limit=80):
    words_list = string.split(" ")
    new_string = ""
    new_text_list = []
    for word in words_list:
        temp = new_string + " " + word
        len_new_string = len(temp)
        if len_new_string >= limit:
            new_text_list.append(new_string)
            new_string = ""
        new_string += " " + word

    return "\n".join(new_text_list)

