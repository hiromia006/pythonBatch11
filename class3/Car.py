class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def startEngine(self):
        print(self.brand, self.model, self.color, "engine started.")

    def stopEngin(self):
        print(self.brand, self.model, self.color, "engine stopped.")


# print("==============================================")
# x = Car()

# print("==============================================")
myCar = Car("Toyota", "Corolla", 2020)
myCar.startEngine()
myCar.stopEngin()
