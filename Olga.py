class Car:
  def __init__(self, wheels, model, speed):
    self.wheels = wheels
    self.model = model
    self.speed = speed
  def getAll (self):
    print ("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")
    pass
class Motocycle(Car):
  def __init__(self,wheels, model, speed,engine):
      super().__init__(wheels, model, speed)
      self.engine = engine
p1=Motocycle(5,"Audi",145,5)
p1.getAll()
