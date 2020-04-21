import random
number = random.randint(1, 10)
counter = 0
limit = 3
while counter < limit:
    guess = int(input("Guess the number:"))
    if guess == number:
        print("You guessed!")
        break
    else:
        counter += 1
        print(f"Try again:{counter}")




