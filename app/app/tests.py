"""Sample test"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Calc test module"""
    def test_add_num(self):
        """Testing adding number Together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """Subtracting numbers logic test"""
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
