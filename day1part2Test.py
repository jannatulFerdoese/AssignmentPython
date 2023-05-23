import unittest
from Day1part2 import operation,module_fuel,fuel_need
class TestFuelCalculation(unittest.TestCase):

    def test_operation(self):
        self.assertEqual(operation(10), 1)
        self.assertEqual(operation(12), 2)
        self.assertEqual(operation(14), 2)

    def test_module_fuel(self):
        self.assertEqual(module_fuel("12\n14\n16"), [2, 2, 2])
        self.assertEqual(module_fuel("12\n-2\n4"), [2, -1, 0])

    def test_fuel_need(self):
        self.assertEqual(fuel_need([12, 14, 16]), [12, 2, 2, 2, 0])
        self.assertEqual(fuel_need([12, -2, 4]), [12, 2, 0, 4, 0])

if __name__ == '__main__':
    unittest.main()

