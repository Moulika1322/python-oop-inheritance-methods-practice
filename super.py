

"""\

class Animal:
    def __init__(self,name):
        self.name=name
    def speaks(self):
        print(f"{self.name} is maling a sounds") 
class Dog(Animal):
    def __init__(self,name,):
        self.name=name
    def speaks(self):
        print(f"{self.name} is a barking")
dog = Dog("julli")
dog.speaks()                   "




class Animal:
    def __init__(self,name):
        self.name = name
    def speaks(self):
        print(f"{self.name} is making sounds")
class Dog(Animal):
    def __init__ (self,name):
        super().__init__(name)
        self.name = name
    def speaks (self):
        super().speaks()
        print(f"{self.name} is barking")  
class Cat(Animal):
    def __init__ (self,name): 
        super().__init__(name)
        self.name = name
    def speaks(self):
        super().speaks()
        print(f"{self.name} is meowing")      


dog = Dog("julli")
dog.speaks() 
cat = Cat("tommy")  
cat.speaks()  








#method overloading: same class ,same method and different poarameters




class A:
    def sum (self,a,b):
        return a+b
    def sum (self,a,b,c):
        return a+b+c
obj = A()
print(obj.sum(2,3,6))


#method overriding : different class ,same mathod and same parameters

class A:
    def display (self):
        print("this is class : A")
class B(A):
    def display (self):
        print("this is class : B")
        super().display()

obj = B()
obj.display()
                


class shape:
    def area (self):
        print ("calculating the areas")

class rectangle(shape):
    def area (self,l,b):
        super().area()
        return l*b
        
class circle(shape):
    def area (self,r):
        super().area()
        return 3.14*r*r

obj=rectangle()
print("area of the rectangle: ",obj.area(4,3))     
obj=circle()
print("area of the circle: ",obj.area(2))




class Vehicle:
    def fuel_efficiency(self):
        print("calculating fuel efficiency...")
class Bike(Vehicle):
    def fuel_efficiency(self,mileage,fueltype):
        super().fuel_efficiency()
        print(f"fuel efficiency :{mileage}km/1,fueltype:{fueltype}") 
class Car(Vehicle):
    def fuel_efficiency(self,mileage):
        super().fuel_efficiency()
        print(f"fuel_efficiency:{mileage}km/1")


obj = Car()
obj.fuel_efficiency(18)

obj = Bike()
obj.fuel_efficiency(22,"petrol")

obj = Car()
obj.fuel_efficiency(40) 


"""
                  
class Application:
    def power_consumption(self):
        print("calculating power consumption...")
class washingmachine(Application):
    def power_consumption(self,power,brand):
        super().power_consumption()
        print(f"power consumption: {power} watts,Brand:{brand}")
class refrigerator(Application):
    def power_consumption(self,power):
        super().power_consumption()
        print(f" power consumption: {power} ")
obj = washingmachine()
obj.power_consumption(1500,"LG")  
obj = refrigerator()
obj.power_consumption(800)                    



