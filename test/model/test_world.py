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
        self.save()


if __name__ == '__main__':
    unittest.main()
