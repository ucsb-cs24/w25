import random

from ..core import Map


def generate(rows, cols, bomb_chance=0.60):
    terrain = Map(rows * 4 + 1, cols * 4 + 1, '#')

    for r in range(rows):
        for c in range(cols):
            lat = 4 * r
            lng = 4 * c

            terrain.fill_rect(lat + 1, lng + 1, 3, 3, '.')
            if random.random() <  bomb_chance:
                terrain[lat+2, lng+2] = '*'

    return terrain

def run_command(args):
    return generate(args.rows, args.cols,
        bomb_chance = args.bomb_chance
    )

def add_command(subparsers):
    parser = subparsers.add_parser('fire-maze')
    parser.set_defaults(func=run_command)

    parser.add_argument('-b', '--bomb-chance', type=float, default=0.60, help='bomb chance (0.00 to 1.00)')
    parser.add_argument('rows', type=int)
    parser.add_argument('cols', type=int)
    return parser
