import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """ Test list of integers """
        data = [1, 2, 3]
        hasil = sum(data)
        self.assertEqual(hasil, 6)


if __name__ == "__main__":
    unittest.main()
