def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be 1 character string.")
    if width <= 2:
        raise Exception("Width must be more than 2.")
    if height <= 2:
        raise Exception("Height must be more than 2.")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (("#", 10, 5), ("0", 20, 10), ("zz", 2, 30), ("s", 3, 1)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print("An exception has happened: " + str(err))
