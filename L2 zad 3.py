age = float(input("Your age:"))
best_lap = float(input("Best lap:"))
if age < 18:
    print("You're not allowed to participate in the race.")
elif age > 65:
    print("You're not allowed to participate in the race.")
elif best_lap >= 47.00:
    print("You're not allowed to participate in the race.")
else:
    print("You are allowed to participate in the race.")
