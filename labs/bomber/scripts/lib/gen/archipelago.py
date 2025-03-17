import random

from ..core import Map, Point

def generate(rows, cols, island_chance=0.90, bridge_chance=0.80, boulder_chance=0.50, bomb_chance=0.60, bomb_radius=2.0):
    islands = Map(rows, cols)
    terrain = Map(13 * rows, 13 * cols, '~')

    for r in range(rows):
        for c in range(cols):
            if random.random() >= island_chance:
                continue

            islands[r, c] = True

            lat = 13 * r + 6
            lng = 13 * c + 6
            terrain.fill_circle(lat, lng, 3.5, '.')

            if random.random() < bomb_chance:
                terrain.fill_circle(
                    (lat - 0.5) + random.random(),
                    (lng - 0.5) + random.random(),
                    bomb_radius * random.random(),
                    '*'
                )

            if islands[r-1, c] and random.random() < bridge_chance:
                for i in range(lat-9, lat-3):
                    if random.random() < boulder_chance:
                        terrain[i, lng] = '#'
                    else:
                        terrain[i, lng] = '.'

            if islands[r, c-1] and random.random() < bridge_chance:
                for i in range(lng-9, lng-3):
                    if random.random() < boulder_chance:
                        terrain[lat, i] = '#'
                    else:
                        terrain[lat, i] = '.'

    return terrain

def run_command(args):
    return generate(args.rows, args.cols,
        island_chance  = args.island_chance,
        bridge_chance  = args.bridge_chance,
        boulder_chance = args.boulder_chance,
        bomb_chance    = args.bomb_chance,
        bomb_radius    = args.bomb_radius
    )

def add_command(subparsers):
    parser = subparsers.add_parser('archipelago')
    parser.set_defaults(func=run_command)

    parser.add_argument('-i', '--island-chance',  type=float, default=0.90, help='island chance (0.00 to 1.00)')
    parser.add_argument('-g', '--bridge-chance',  type=float, default=0.80, help='bridge chance (0.00 to 1.00)')
    parser.add_argument('-s', '--boulder-chance', type=float, default=0.50, help='boulder chance (0.00 to 1.00)')
    parser.add_argument('-b', '--bomb-chance',    type=float, default=0.60, help='bomb chance (0.00 to 1.00)')
    parser.add_argument('-r', '--bomb-radius',    type=float, default=2.00, help='bomb radius')
    parser.add_argument('rows', type=int)
    parser.add_argument('cols', type=int)
    return parser
