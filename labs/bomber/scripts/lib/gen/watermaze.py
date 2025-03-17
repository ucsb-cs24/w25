import random

from ..core import Point, Map
from .mst   import prims


def generate(rows, cols, islands=2, loop_chance=0.10):
    vertices = prims(rows, cols, seeds=islands, loop_chance=loop_chance)
    terrain  = Map(rows * 4 + 2, cols * 4 + 2, '~')
    for point in vertices.points():
        djs = vertices[point]
        r   = 4 * point.lat + 1
        c   = 4 * point.lng + 1

        if djs.south:
            terrain.fill_rect(r+3, c+1, 2, 2, '.')
        if djs.east:
            terrain.fill_rect(r+1, c+3, 2, 2, '.')
        terrain.fill_rect(r+1, c+1, 2, 2, '.')

    return terrain

def run_command(args):
    return generate(args.rows, args.cols,
        islands     = args.islands,
        loop_chance = args.loop_chance
    )

def add_command(subparsers):
    parser = subparsers.add_parser('water-maze')
    parser.set_defaults(func=run_command)
    parser.add_argument('-n', '--islands',     type=int,   default=2,    help='number of islands')
    parser.add_argument('-l', '--loop-chance', type=float, default=0.10, help='loop chance (0.00 to 1.00)')
    parser.add_argument('rows', type=int)
    parser.add_argument('cols', type=int)
    return parser
