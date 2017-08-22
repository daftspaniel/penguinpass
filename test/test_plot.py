import unittest
from thepass.plot import Plot


class TestPlot(unittest.TestCase):
    def setUp(self):
        pass

    def test_ctor(self):
        self.plot = Plot()
        self.assertEqual(self.plot.visited, False)


if __name__ == '__main__':
    unittest.main()
