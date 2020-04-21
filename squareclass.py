class Square:
    def __init__(self, side):
        self.side = side

    def __pow__(square_one, square_two):
        return square_one.side ** square_two.side


squareOne = Square(3)
squareTwo = Square(2)

print(squareOne.__pow__(squareTwo))
