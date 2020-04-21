lst_2 = []
for i in range(0, 1):
    for b in range(0, 9):
            b += 1
            lst_2.append("*")
            if b > 5:
                lst_2 = lst_2[:-2]
            print(str(lst_2))
