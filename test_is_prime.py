
import unittest

import prime_examer

# python3 -m unittest -v <test_example.y>


class UnitTest(unittest.TestCase):

    def test_is_prime(self):
        class Tester:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants

        testers = []

        testers.append(Tester(123, False))
        testers.append(Tester(223, True))
        testers.append(Tester(117, False))
        testers.append(Tester(613, True))
        testers.append(Tester(143, False))
        testers.append(Tester(846, False))
        testers.append(Tester(1151, True))

        for tester in testers:
            try:
                self.assertEqual(prime_examer.is_prime(
                    tester.args), tester.wants)
            except:
                print("result of {} is not {}".format(
                    tester.args, tester.wants))


if __name__ == '__main__':
    unittest.main()
