import random

from ..core import Map, Point


# class Grid(Map):
#     def __init__(self, height, width):
#         super().__init__(height, width)
#         for point in self.points():
#             self[point] = GridCell(point)


class DisjointSet:
    def __init__(self, parent=None):
        self.parent = parent
        self.count  = 1

    def find(self):
        if self.parent is None:
            return self
        self.parent = self.parent.find()
        return self.parent

    def solo(self):
        return self.find().count == 1

    def union(self, other):
        sparent = self.find()
        oparent = other.find()
        if sparent is not oparent:
            sparent.parent = oparent
            oparent.count += sparent.count
            return True
        return False


class GridCell(DisjointSet):
    def __init__(self, point):
        super().__init__()
        self.point = point
        self.north = None
        self.west  = None
        self.south = None
        self.east  = None

    def connect(self, other, edge=True):
        if self.point.lng == other.point.lng:
            if self.point.lat == other.point.lat - 1:
                self.south  = edge
                other.north = edge
            elif self.point.lat == other.point.lat + 1:
                self.north  = edge
                other.south = edge
        if self.point.lat == other.point.lat:
            if self.point.lng == other.point.lng - 1:
                self.east   = edge
                other.west  = edge
            elif self.point.lng == other.point.lng + 1:
                self.west   = edge
                other.east  = edge


class RandomQueue:
    def __init__(self, data=[]):
        self.data = list(data)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        index = random.randrange(len(self.data))
        value = self.data[index]
        self.data[index] = self.data[-1]
        self.data.pop()
        return value

    def __len__(self):
        return len(self.data)

def fragments(height, width, extra_chance=0.00):
    vertices = Map(height, width)
    edges    = RandomQueue()

    for point in vertices.points():
        vertices[point] = GridCell(point)
        if point.lat > 0:
            other = Point(point.lat - 1, point.lng)
            edges.push((other, point))
        if point.lng > 0:
            other = Point(point.lat, point.lng - 1)
            edges.push((other, point))

    while len(edges) > 0:
        src, dst = edges.pop()
        sset = vertices[src]
        dset = vertices[dst]

        if sset.solo() or dset.solo() or random.random() < extra_chance:
            sset.connect(dset)
            sset.union(dset)

    return vertices


def kruskals(height, width, loop_chance=0.00):
    vertices = Map(height, width)
    edges    = RandomQueue()

    for point in vertices.points():
        vertices[point] = GridCell(point)
        if point.lat > 0:
            other = Point(point.lat - 1, point.lng)
            edges.push((other, point))
        if point.lng > 0:
            other = Point(point.lat, point.lng - 1)
            edges.push((other, point))

    while len(edges) > 0:
        src, dst = edges.pop()

        if not vertices[src].union(vertices[dst]):
            if random.random() >= loop_chance:
                continue

        vertices[src].connect(vertices[dst])

    return vertices


def prims(height, width, seeds=1, loop_chance=0.00):
    vertices = Map(height, width)
    queue    = RandomQueue()
    seedset  = set()

    while len(seedset) < seeds:
        point = vertices.randpoint()
        if point not in seedset:
            for neighbor in vertices.neighbors(point):
                queue.push((point, neighbor))
            vertices[point] = GridCell(point)
            seedset.add(point)

    while len(queue) > 0:
        src, dst = queue.pop()

        sset = vertices[src]
        dset = vertices[dst]

        if dset is None:
            # New ground; claim it!
            dset = GridCell(dst)
            vertices[dst] = dset
        elif sset.find() is not dset.find():
            # Separate regions; keep 'em separate.
            continue
        elif random.random() < loop_chance:
            # Same region; maybe add a loop.
            pass
        else:
            continue

        sset.union(dset)
        sset.connect(dset)
        for neighbor in vertices.neighbors(dst):
            queue.push((dst, neighbor))

    return vertices
