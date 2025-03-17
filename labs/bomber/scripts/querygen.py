#! /usr/bin/env python3

import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, default=10)
    parser.add_argument('-s', '--src-types', default='.*')
    parser.add_argument('-d', '--dst-types', default='.*#')
    parser.add_argument('-r', '--seed', type=int)
    parser.add_argument('map_file')
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    width = None
    srcs  = []
    dsts  = []

    with open(args.map_file) as file:
        for lat, line in enumerate(file):
            line = line.rstrip('\r\n')
            if width is None:
                width = len(line)
            elif len(line) != width:
                print('ERROR: Not all lines as the same length.')
                exit(1)

            for lng, c in enumerate(line):
                if c not in '.#~*':
                    print('ERROR: Invalid character %r in file.' % c)
                    exit(1)

                if c in args.src_types:
                    srcs.append((lat, lng))
                if c in args.dst_types:
                    dsts.append((lat, lng))

    if not srcs:
        print('ERROR: No valid starting points found.')
        exit(1)
    if not dsts:
        print('ERROR: No valid destinations found.')
        exit(1)

    for i in range(args.number):
        src = random.choice(srcs)
        dst = random.choice(dsts)
        print('%d\t%d\t\t%d\t%d' % (*src, *dst))


if __name__ == '__main__':
    main()
