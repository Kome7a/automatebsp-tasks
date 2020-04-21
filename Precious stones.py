import random
import time
import os


class Stone:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __repr__(self):
        return f" {self.number} - " + self.name


class Pocket:
    MAX_ITEMS_IN_POCKET = 5

    def __init__(self, stones=None):
        if stones is None:
            stones = []
        self.stones = stones

    def take_stone(self, stone):
        if len(self.stones) <= self.MAX_ITEMS_IN_POCKET:
            self.stones.append(stone)
        else:
            self.stones[0] = stone


st1 = Stone("Emerald", 1)
st2 = Stone("Mistress", 2)
st3 = Stone("Diamond", 3)
st4 = Stone("Lilac", 4)
st5 = Stone("Green", 5)
st6 = Stone("Topaz", 6)
st7 = Stone("Blue", 7)
st8 = Stone("Jackie", 8)
st9 = Stone("Sun", 9)
st10 = Stone("Dream", 10)

stones1 = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]
pocket1 = Pocket()

while True:
    time.sleep(2)
    random_stone = random.choice(stones1)
    pocket1.take_stone(random_stone)
    print(pocket1.stones)






