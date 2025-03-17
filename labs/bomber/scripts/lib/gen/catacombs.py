from ..core import Map
from .mst   import fragments

def generate(rows, cols, extra_chance=0.03):
    vertices = fragments(rows, cols, extra_chance)
    terrain  = Map(5 * rows, 5 * cols, '#')

    for r in range(rows):
        for c in range(cols):
            lat = 5 * r + 2
            lng = 5 * c + 2

            if vertices[r, c].south:
                terrain.fill_rect(lat, lng, 6, 1, '.')
            if vertices[r, c].east:
                terrain.fill_rect(lat, lng, 1, 6, '.')
            terrain[lat, lng] = '*'

    return terrain

def run_command(args):
    return generate(args.rows, args.cols,
        extra_chance = args.extra_chance
    )

def add_command(subparsers):
    parser = subparsers.add_parser('catacombs')
    parser.set_defaults(func=run_command)

    parser.add_argument('-e', '--extra-chance', type=float, default=0.03, help='extra chance (0.00 to 1.00)')
    parser.add_argument('rows', type=int)
    parser.add_argument('cols', type=int)
    return parser
