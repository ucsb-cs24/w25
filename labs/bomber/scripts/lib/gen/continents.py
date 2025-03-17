import random

from ..core import Point, Map


def average(*args):
    total = 0
    count = 0
    for arg in args:
        if arg is not None:
            total += arg
            count += 1
    return total / count

def tryget(map, lat, lng):
    if lat < 0 or lat >= map.height:
        return None
    if lng < 0 or lng >= map.width:
        return None

    return map[lat, lng]

# https://en.wikipedia.org/wiki/Diamond-square_algorithm
def generate(rows, cols, scale=3, noise=0.5, falloff=0.55, bomb_chance=0.01):
    d = 2 ** scale
    H = d * rows + 1
    W = d * cols + 1

    elevation = Map(H, W)
    terrain   = Map(H, W)

    for lat in range(0, H, d):
        for lng in range(0, W, d):
            # elevation[lat, lng] = 2 * random.random() - 1
            elevation[lat, lng] = random.gauss(0.0, noise)

    while d > 1:
        # Fill in squares...
        for lat in range(d//2, H, d):
            for lng in range(d//2, W, d):
                nw = tryget(elevation, lat - d//2, lng - d//2)
                sw = tryget(elevation, lat + d//2, lng - d//2)
                se = tryget(elevation, lat + d//2, lng + d//2)
                ne = tryget(elevation, lat - d//2, lng + d//2)

                avg  = average(nw, sw, se, ne)
                avg += random.gauss(0.0, noise)
                elevation[lat, lng] = avg

        # Fill in diamonds...
        olng = d//2
        for lat in range(0, H, d//2):
            for lng in range(olng, W, d):
                n = tryget(elevation, lat - d//2, lng)
                w = tryget(elevation, lat, lng - d//2)
                s = tryget(elevation, lat + d//2, lng)
                e = tryget(elevation, lat, lng + d//2)

                avg  = average(n, w, s, e)
                avg += noise * (2 * random.random() - 1)
                elevation[lat, lng] = avg
            olng ^= d//2

        noise *= falloff
        d //= 2

    for lat in range(H):
        for lng in range(W):
            elev = elevation[lat, lng]

            if elev < -0.45:
                terrain[lat, lng] = '~'
            elif elev > 0.45:
                terrain[lat, lng] = '#'
            elif random.random() < bomb_chance:
                terrain[lat, lng] = '*'
            else:
                terrain[lat, lng] = '.'

    return terrain

def run_command(args):
    return generate(args.rows, args.cols,
        scale       = args.scale,
        noise       = args.noise,
        falloff     = args.falloff,
        bomb_chance = args.bomb_chance
    )

def add_command(subparsers):
    parser = subparsers.add_parser('continents')
    parser.set_defaults(func=run_command)

    parser.add_argument('-s', '--scale',       type=int,   default=3,    help='tile size (2^s)')
    parser.add_argument('-n', '--noise',       type=float, default=0.95, help='randomness')
    parser.add_argument('-f', '--falloff',     type=float, default=0.55, help='randomness falloff (0.00 to 1.00)')
    parser.add_argument('-b', '--bomb-chance', type=float, default=0.05, help='bomb chance (0.00 to 1.00)')
    parser.add_argument('rows', type=int)
    parser.add_argument('cols', type=int)
    return parser
