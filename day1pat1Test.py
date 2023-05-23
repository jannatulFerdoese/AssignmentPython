import unittest
from Day1part1 import fuel, sum_fuel_required


class TestFuelCalculations(unittest.TestCase):
    def test_fuel_required(self):
        self.assertEqual(fuel(12), 2)
        self.assertEqual(fuel(14), 2)
        self.assertEqual(fuel(1969), 654)
        self.assertEqual(fuel(100756), 33583)

    def test_total_fuel_required(self):
        self.assertEqual(sum_fuel_required([12, 14, 1969, 100756]), 34241)


if __name__ == '__main__':
    unittest.main()