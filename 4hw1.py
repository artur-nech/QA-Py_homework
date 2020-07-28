class car:
    def __init__(self, tires, model, speed):
        self.tires = tires
        self.model = model
        self.speed = speed

    def check_car(bus):
        print(bus.tires, bus.model, bus.speed)


ford = car('pirelly', 'fordSpeed', 210)
ford.check_car()

print(ford.tires)
print('maximum speed ',ford.speed)
