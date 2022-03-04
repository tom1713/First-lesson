
import unittest

import car

# python3 -m unittest -v <test_example.y>


class UnitTest(unittest.TestCase):
    def test_car_encapsulation(self):

        car_1 = car.Car(111, 2, 'red')

        try:
            print(car_1.__engin_number)
        except:
            print("Access Error")
            car_1.show_engin_number()

        car_1.set_engin_number(333)
        car_1.show_engin_number()


if __name__ == '__main__':
    unittest.main()
