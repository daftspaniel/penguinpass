class World(object):
    def __init__(self, width=64, height=64):
        self.name = 'Default'
        self.width = width
        self.height = height
        self._mapData = None

    def generate(self):
        """ Generate empty map"""
        self._mapData = [[{}] * self.width for x in range(self.height)]
