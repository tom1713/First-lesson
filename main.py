
import car

car_1 = car.Car(111, 2, 'red')

try:
    print(car_1.__engin_number)
except:
    print("Access Error")
    print(car_1.get_engin_number())

car_1.set_engin_number(333)
print(car_1.get_engin_number())
