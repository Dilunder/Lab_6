import unittest
from calc import resulting_expression

class CalculatorTest(unittest.TestCase):
    def test_eval_expression(self):
        self.assertEqual(resulting_expression('7-2'), 7 - 5)
        self.assertEqual(resulting_expression('5*5'), 5 * 5)
        self.assertEqual(resulting_expression('12/3'), 12 / 3)
        self.assertEqual(resulting_expression('1+1'), 1 + 1)
        self.assertEqual(resulting_expression('1-2'), 1 - 2)
        self.assertEqual(resulting_expression('1*0'), 1 * 0)
        self.assertEqual(resulting_expression('1/0'), "Division by zero!")

if __name__ == '__main__':
    unittest.main()
