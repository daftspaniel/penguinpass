class World(object):
    def __init__(self, width=64, height=64):
        self._name = 'Default'
        self._width = width
        self._height = height
        self._mapData = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def name(self):
        return self._name

    def generate(self):
        """ Generate empty map"""
        self._mapData = [[{}] * self._height for x in range(self._width)]

    def size(self):
        return self.width, self.height
