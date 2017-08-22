class World(object):
    def __init__(self, width=64, height=64):
        self._name = 'Default'
        self.width = width
        self.height = height
        self._mapData = None

    @property
    def name(self):
        return self._name

    def generate(self):
        """ Generate empty map"""
        self._mapData = [[{}] * self.height for x in range(self.width)]

    def size(self):
        return len(self._mapData), len(self._mapData[0])
