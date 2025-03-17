#! /usr/bin/env python3

import random

from .core import Point


class ParseError(Exception):
    pass

class PointError(Exception):
    pass

class RouteError(Exception):
    pass


class Validator:
    def __init__(self, lines):
        if not lines or not lines[0]:
            raise ParseError('Empty map!')

        self.lines  = lines
        self.width  = len(lines[0])
        self.height = len(lines)

        for r, line in enumerate(lines, 1):
            if len(line) != self.width:
                raise ParseError('Line %d contains %d characters (expected %d)!' % (r, len(line), self.width))
            for c, terrain in enumerate(line, 1):
                if terrain not in '.#*~':
                    raise ParseError('Invalid character at line %d column %d: %r' % (r, c, terrain))

    @classmethod
    def load(cls, filename):
        with open(filename) as file:
            lines = [line.rstrip('\r\n') for line in file]
            return cls(lines)

    def __getitem__(self, point):
        return self.lines[point[0]][point[1]]

    def check_point(self, point):
        if point[0] < 0 or point[0] >= self.height:
            return False
        if point[1] < 0 or point[1] >= self.width:
            return False
        return True

    def validate_point(self, point):
        if not self.check_point(point):
            raise PointError('Point is out of bounds: ' + str(point))

    def validate_route(self, src, dst, route):
        if not self.check_point(src):
            raise PointError('Starting point is out of bounds.')
        if not self.check_point(dst):
            raise PointError('Destination is out of bounds.')

        point = Point(src.lat, src.lng)
        clear = set()
        bombs = 0

        terrain = self[src]
        if terrain == '~':
            raise PointError('Starting point is in the water.')
        if terrain == '#':
            raise PointError('Starting point is on a boulder.')
        if terrain == '*':
            clear.add(point)
            bombs += 1

        for c in route:
            if c == 'n':
                point = Point(point.lat - 1, point.lng)
            elif c == 'e':
                point = Point(point.lat, point.lng + 1)
            elif c == 's':
                point = Point(point.lat + 1, point.lng)
            elif c == 'w':
                point = Point(point.lat, point.lng - 1)
            else:
                raise('Invalid character in route: %r' % c)

            if not self.check_point(point):
                raise RouteError('Walked off the edge of the map!')

            if point in clear:
                continue
            terrain = self[point.lat, point.lng]

            if terrain == '*':
                clear.add(point)
                bombs += 1
            elif terrain == '#':
                if bombs <= 0:
                    raise RouteError('Walked into a boulder with no bombs!')
                clear.add(point)
                bombs -= 1
            elif terrain == '~':
                raise RouteError('Walked into the water!')

        if point != dst:
            raise RouteError('Route does not end at destination!')
