class Car:
    def __init__(self, car_type: str, day_price: int):
        self.car_type = car_type
        self.day_price = day_price

    def __repr__(self):
        return self.car_type + " - " + str(self.day_price)


class Dealership:
    def __init__(self, cars: list, location, margin):
        self.cars = cars
        self.available_cars = []
        self.rented_cars = []
        self.location = location
        self.margin = margin

    def rent_car(self, car, days):
        if car in self.available_cars:
            self.rented_cars.append(car)
            return self.bill(car, days)

    def bill(self, car, days):
        return car.day_price * days * self.margin

    def __repr__(self):
        return f"{self.cars}"


def main():
    suv = Car("SUV", 100)
    sedan = Car("Sedan", 50)
    hatchback = Car("Hatchback", 30)

    cars = [suv, sedan, hatchback]
    my_dealership = Dealership(cars, 'Sofia', 1.05)

    # print choices
    for num, car in enumerate(cars, start=1):
        print(f"Press - {num} to rent: {car}")

    # ask customer for choice

    customer_pick = None
    while not customer_pick:
        customer_pick = int(input("Choose a car:"))
        if customer_pick == 1:
            customer_pick = cars[0]
        elif customer_pick == 2:
            customer_pick = cars[1]
        elif customer_pick == 3:
            customer_pick = cars[2]
        else:
            customer_pick = None

    days = 0
    while True:
        days = int(input("For how many days:"))
        if days <= 0:
            print("You should rent for at least a day.")
        else:
            print(my_dealership.bill(customer_pick, days))
            print(my_dealership.rented_cars)
            break


main()
