#! /usr/bin/env python3

import random

from lib import gen


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', type=int, help='random seed')

    subparsers = parser.add_subparsers(dest='command', required=True, help='map style')
    gen.archipelago.add_command(subparsers)
    gen.catacombs.add_command(subparsers)
    gen.continents.add_command(subparsers)
    gen.firemaze.add_command(subparsers)
    gen.swisscheese.add_command(subparsers)
    gen.watermaze.add_command(subparsers)

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    terrain = args.func(args)
    for row in terrain.data:
        print(''.join(row))


if __name__ == '__main__':
    main()
