import unittest


class TestNumbers(unittest.TestCase):
    def test_summa(self):
        self.a = [2, 6, 4]
        result = sum(self.a)
        self.assertEqual(12, result)

    def test_average(self):
        self.a = [2, 6, 4]
        result = sum(self.a) / len(self.a)
        self.assertEqual(4, result)

    def test_min(self):
        self.a = [2, -6, 4]
        result = min(self.a)
        self.assertEqual(-6, result)

    def test_max(self):
        self.a = [2, 6, 4]
        result = max(self.a)
        self.assertEqual(6, result)


if __name__ == '__main__':
    unittest.main()
