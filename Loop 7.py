numbers = list(range(0, 50))
for i in numbers:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        i = str("BOTH")
    elif i % 5 == 0:
        i = str("FIVE")
    elif i % 3 == 0:
        i = str("THREE")
    print(i)
