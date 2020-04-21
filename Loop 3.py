dict_1 = {
    "Ivan Ivanov": "+359884545454",
    "Gergana Ivanova": "+359887777777"
}

for name, number in dict_1.items():
    new = (number[0:4].replace("+359", "00") + number[4:])
    print(f"{name} mobile number is {new}")
