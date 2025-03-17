#! /usr/bin/env python3

import argparse

from lib.core      import Point
from lib.validator import PointError, RouteError, Validator

def read_point(prompt):
    text = input(prompt)
    lat, lng = (int(x) for x in text.split())
    return Point(lat, lng)

def run_interactive(validator):
    while True:
        src = read_point('src> ')
        if not src: break

        dst = read_point('dst> ')
        if not dst: break

        route = input('route> ')
        validate(validator, src, dst, route)

def run_query_file(validator, query_file, prompts=True):
    with open(query_file) as file:
        for line in file:
            slat, slng, dlat, dlng = (int(x) for x in line.split())
            src = Point(slat, slng)
            dst = Point(dlat, dlng)

            print('query: %s => %s' % (src, dst))
            route = input('route> ' if prompts else '')
            validate(validator, src, dst, route)

def validate(validator, src, dst, route):
    try:
        validator.validate_route(src, dst, route)
        print('OK')
    except PointError as e:
        print('Bad Point: ' + str(e))
    except RouteError as e:
        print('Bad Route: ' + str(e))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--no-prompts', action='store_true')
    parser.add_argument('-q', '--query-file')
    parser.add_argument('map_file')
    args = parser.parse_args()

    validator = Validator.load(args.map_file)

    try:
        if args.query_file:
            run_query_file(validator, args.query_file, not args.no_prompts)
        else:
            run_interactive(validator)
    except KeyboardInterrupt:
        print('')
    except EOFError:
        print('')


if __name__ == '__main__':
    main()
