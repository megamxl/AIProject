import unittest

from Heuristics import Hamming


class HammingTests(unittest.TestCase):

    def test_distanceCalc(self):
        distance0 = Hamming.Hamming.calc([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        distance8 = Hamming.Hamming.calc([[8, 7, 6], [5, 2, 3], [4, 1, 0]])
        distance5 = Hamming.Hamming.calc([[0, 1, 2], [3, 5, 4], [7, 8, 6]])

        self.assertEqual(0, distance0)
        self.assertEqual(8, distance8)
        self.assertEqual(5, distance5)


if __name__ == '__main__':
    unittest.main()
