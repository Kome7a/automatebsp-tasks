tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(data):
    widths = []
    for lst in data:
        width = len(max(lst, key=len))
        widths.append(width)
    for x in range(len(data[0])):
        for y in range(len(data)):
            print(data[y][x].rjust(widths[y]), end=" ")
        print("")


print_table(tableData)
