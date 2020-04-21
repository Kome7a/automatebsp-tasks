name = "Evgeni"
meet_point = len(name) // 2
for a, b in name:
    a = meet_point - a
    b = meet_point + b
    print(a, b)
