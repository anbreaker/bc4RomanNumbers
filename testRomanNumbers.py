import unittest
from romanNumbers import romano_a_arabigo
from unittest.mock import patch


class RomanNumberTest(unittest.TestCase):
    def test_symbol_roman(self):
        self.assertEqual(romano_a_arabigo('I'), 1)
        self.assertEqual(romano_a_arabigo('V'), 5)
        self.assertEqual(romano_a_arabigo('X'), 10)
        self.assertEqual(romano_a_arabigo('L'), 50)
        self.assertEqual(romano_a_arabigo('C'), 100)
        self.assertEqual(romano_a_arabigo('D'), 500)
        self.assertEqual(romano_a_arabigo('M'), 1000)
        self.assertEqual(romano_a_arabigo('A'), 0)

    def test_numeros_crecientes(self):
        self.assertEqual(romano_a_arabigo('III'), 3)
        self.assertEqual(romano_a_arabigo('IIII'), 0)
        self.assertEqual(romano_a_arabigo('XVI'), 16)
        self.assertEqual(romano_a_arabigo('XXIII'), 23)
        self.assertEqual(romano_a_arabigo('CCC'), 300)

    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(romano_a_arabigo('LXXIII'), 73)
        self.assertEqual(romano_a_arabigo('IIII'), 0)
        self.assertEqual(romano_a_arabigo('CCCC'), 0)

    def test_numeros_decrecientes(self):
        self.assertEqual(romano_a_arabigo('XCIX'), 99)
        self.assertEqual(romano_a_arabigo('CMXCIX'), 999)
        self.assertEqual(romano_a_arabigo('MMCMLXIX'), 2969)
        self.assertEqual(romano_a_arabigo('VC'), 0)
        self.assertEqual(romano_a_arabigo('MVL'), 0)


if __name__ == '__main__':
    unittest.main()
