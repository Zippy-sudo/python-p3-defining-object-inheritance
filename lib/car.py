from vehicle import Vehicle

class Car(Vehicle):
    
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

a = Car(22, 12)
print(a)
