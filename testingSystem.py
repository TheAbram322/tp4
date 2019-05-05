import unittest
import minChange


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(minChange.min_change('1231'), 3)

    def test_sub(self):
        self.assertEqual(minChange.min_change('adgdsx'), 5)

    def test_mul(self):
        self.assertEqual(minChange.min_change('aba'), 0)

    def test_div(self):
        self.assertEqual(minChange.min_change('abracadabra'), 10)


if __name__ == '__main__':
    unittest.main()
