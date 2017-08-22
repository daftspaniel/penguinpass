import unittest
from thepass.world import World


class TestWorld(unittest.TestCase):
    def setUp(self):
        pass

    def test_ctor(self):
        self.world = World()
        self.assertEqual(self.world.name, 'Default')

    def test_generate(self):
        self.world = World(64, 128)
        self.world.generate()
        self.assertEqual(self.world.width, 64)
        self.assertEqual(self.world.height, 128)


if __name__ == '__main__':
    unittest.main()
