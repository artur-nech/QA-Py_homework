class Car:
    wheels = 4
    model = 'Some'
    speed = 123,5
    def __init__(self, wheels, model, speed):
     self.model=model
     self.speed=speed
     self.wheels=wheels
    def myPrint(auto):
        print("This is ", auto.model)
Audi=Car(5,"Au",150)
print(Audi.wheels,Audi.speed)
