import random

from ..core import Point, Map


def generate(rows, cols, hole_chance=0.95, min_radius=2, max_radius=4.5, bomb_chance=0.95, bomb_radius=1.5):
    W = 7
    terrain = Map(W * rows, W * cols, '#')

    for r in range(rows):
        for c in range(cols):
            lat = W * (r + random.random())
            lng = W * (c + random.random())
            rad = random.random() * (max_radius - min_radius) + min_radius
            terrain.fill_circle(lat, lng, rad, '.')

            if random.random() < bomb_chance:
                bmb = random.random() * bomb_radius
                terrain.fill_circle(lat, lng, bmb, '*')

    return terrain

def run_command(args):
    return generate(args.rows, args.cols,
        hole_chance = args.hole_chance,
        min_radius  = args.min_radius,
        max_radius  = args.max_radius,
        bomb_chance = args.bomb_chance,
        bomb_radius = args.bomb_radius
    )

def add_command(subparsers):
    parser = subparsers.add_parser('swiss-cheese')
    parser.set_defaults(func=run_command)

    parser.add_argument('-c', '--hole-chance', type=float, default=0.95, help='hole chance (0.00 to 1.00)')
    parser.add_argument('-m', '--min-radius',  type=float, default=2.00, help='minimum hole radius')
    parser.add_argument('-M', '--max-radius',  type=float, default=4.50, help='maximum hole radius')
    parser.add_argument('-b', '--bomb-chance', type=float, default=0.95, help='bomb chance (0.00 to 1.00)')
    parser.add_argument('-r', '--bomb-radius', type=float, default=1.50, help='bomb radius')
    parser.add_argument('rows', type=int)
    parser.add_argument('cols', type=int)
    return parser
