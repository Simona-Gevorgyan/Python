class Vehicle:
    def init(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def str(self):
        return f"{self.make} {self.model} ({self.year})"
