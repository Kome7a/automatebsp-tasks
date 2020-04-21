def max_min(numbers: list):
    try:
        max_num = numbers[0]
        min_num = numbers[0]
        for item in numbers:
            if item > max_num:
                max_num = item
            if item < min_num:
                min_num = item
        min_max = (min_num, max_num)
    except IndexError as error:
        raise IndexError
    return min_max


my_list = []
print(max_min(my_list))

