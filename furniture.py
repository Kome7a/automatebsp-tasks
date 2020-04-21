class Furniture:
    def __init__(self):
        self.wood = "Teakwood"


class Chair(Furniture):
    def __init__(self):
        super().__init__()

    @classmethod
    def chair_legs(cls):
        return 4


def main():
    my_chair = Chair()

    print("Would you like to change type of wood? Y/N")
    wood_change = input()
    if wood_change == "n":
        print(f"The chair you've ordered will be made of {my_chair.wood} and will have {my_chair.chair_legs()} legs.")
    elif wood_change == "y":
        my_chair.wood = input("Type the type of wood you'd like to order:")
        print(f"The chair you've ordered will be made of {my_chair.wood} and will have {my_chair.chair_legs()} legs.")
    print(my_chair.wood)
    return my_chair



main()
