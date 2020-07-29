#2. Создание полей класса
#Создайте пустой класс без методов и полей.
#На основе класса создайте два объекта. Обратитесь ко второму объекту и
# создайте для него поле «newValue» со значением 5.
#
class car:
    def __init__(*arg):
        

class bus(car):
    def __init__(*arg):
    pass

class sedan(car):
    def __init__(*arg):
    pass

ford = sedan('pirelly', 'fordSpeed', 210)
ford.check_car()

print(ford.tires)
print('maximum speed ',ford.speed)
