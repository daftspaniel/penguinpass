from thepass.model.plot import Plot


class WorldTime(object):
    def __init__(self):
        self._day = 130
        self._season = 1

    def progress(self):
        self._day += 1
        if self._day < 90:
            self._season = 0
        elif self._day < 89 and self._day < 181:
            self._season = 1
        elif self._day > 180 and self._day < 261:
            self._season = 2
        else:
            self._season = 3

class World(object):
    def __init__(self, width: int = 64, height: int = 64):
        self._name = 'Default'
        self._width = width
        self._height = height
        self._mapData = None
        self._worldTime = WorldTime()

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
        self._mapData = [[Plot(1)] * self._height for x in range(self._width)]

    def size(self):
        return self.width, self.height

    def save(self):
        print("Not implemented.")

    def __str__(self):
        out = ""
        for col in self._mapData:
            for item in col:
                out += str(item.type)
            out += '\n'
        return out
