import unittest

from thepass.model.world import World


class TestWorld(unittest.TestCase):
    def setUp(self):
        pass

    def test_ctor(self):
        self.world = World()
        self.assertEqual(self.world._name, 'Default')

    def test_generate(self):
        self.world = World(64, 128)
        self.world.generate()
        width, height = self.world.size()
        self.assertEqual(width, 64)
        self.assertEqual(height, 128)

    def test_save(self):
        self.world = World()
        self.world.save()

    def test_str(self):
        self.world = World(2, 3)
        self.world.generate()
        self.assertEqual("111\n111\n", str(self.world))


if __name__ == '__main__':
    unittest.main()
