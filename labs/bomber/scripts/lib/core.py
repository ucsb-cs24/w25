import collections
import math
import random

PointBase = collections.namedtuple('Point', ['lat', 'lng'])

class Point(PointBase):
    def __str__(self):
        return '(%d, %d)' % self


class Map:
    def __init__(self, height, width, fill=None):
        self.data   = [[fill] * width for _ in range(height)]
        self.height = height
        self.width  = width

    def __getitem__(self, point):
        return self.data[point[0]][point[1]]

    def __setitem__(self, point, fill):
        self.data[point[0]][point[1]] = fill

    def fill_circle(self, lat, lng, radius, fill):
        minlat = max(math.floor(lat - radius), 0)
        maxlat = min(math.ceil( lat + radius), self.height)
        minlng = max(math.floor(lng - radius), 0)
        maxlng = min(math.ceil( lng + radius), self.width)

        r2 = radius * radius
        for r in range(minlat, maxlat):
            dr2 = (r - lat) * (r - lat)
            for c in range(minlng, maxlng):
                dc2 = (c - lng) * (c - lng)
                if dr2 + dc2 < r2:
                    self.data[r][c] = fill

    def fill_rect(self, lat, lng, height, width, fill):
        minlat = max(lat, 0)
        maxlat = min(lat + height, self.height)
        minlng = max(lng, 0)
        maxlng = min(lng + width,  self.width)

        for r in range(minlat, maxlat):
            for c in range(minlng, maxlng):
                self.data[r][c] = fill

    def neighbors(self, point):
        if point.lat > 0:
            yield Point(point.lat - 1, point.lng)
        if point.lat + 1 < self.height:
            yield Point(point.lat + 1, point.lng)
        if point.lng > 0:
            yield Point(point.lat, point.lng - 1)
        if point.lng + 1 < self.width:
            yield Point(point.lat, point.lng + 1)

    def points(self):
        for lat in range(self.height):
            for lng in range(self.width):
                yield Point(lat, lng)

    def randpoint(self):
        lat = random.randrange(self.height)
        lng = random.randrange(self.width)
        return Point(lat, lng)
