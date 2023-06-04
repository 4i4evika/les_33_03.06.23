import unittest
from number import Number


class TestNumbers(unittest.TestCase):
    def test_oct(self):
        result = Number.oct_number(123)[2:]
        self.assertEqual('173', result)

    def test_hex(self):
        result = Number.hex_number(123)[2:]
        self.assertEqual('7b', result)

    def test_bin(self):
        result = Number.bin_number(123)[2:]
        self.assertEqual('1111011', result)


if __name__ == '__main__':
    unittest.main()
