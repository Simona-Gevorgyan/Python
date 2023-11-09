from Vehicle import Vehicle

class Car(Vehicle):
    def init(self, make, model, year, doors):
        super().init(make, model, year)
        self.doors = doors

class Plane(Vehicle):
    def init(self, make, model, year, wings):
        super().init(make, model, year)
        self.wings = wings

class Boat(Vehicle):
    def init(self, make, model, year, hull):
        super().init(make, model, year)
        self.hull = hull

class RaceCar(Car):
    def init(self, make, model, year, doors, top_speed):
        super().init(make, model, year, doors)
        self.top_speed = top_speed

toyota_corolla = Car("Toyota", "Corolla", 2021, 4)
boeing_747 = Plane("Boeing", "747", 2000, 4)
sea_doo_spark = Boat("Sea-Doo", "Spark", 2022, 1)
lamborghini_urus = RaceCar("Lamborghini", "Urus", 2015, 2, 200)

print(toyota_corolla)
print(boeing_747)
print(sea_doo_spark)
print(lamborghini_urus)
