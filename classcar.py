class Car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model 
        self.colour = colour 
        self.km = 0
    
    def add_mileage(self):
        km = int(input())
        self.km += km 
        return self.km

    def get_total_mileage(self):
        return self.km

car1 = Car('Volvo', "xc60", 'blue')

print(car1.brand)
car1.add_mileage()
car1.add_mileage()
print(car1.get_total_mileage())