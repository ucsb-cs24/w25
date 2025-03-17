# Bomber Scripts

## `generate.py`

This is a wrapper script around all the random layout engines I used to generate
the performance tests. If you want to generate similar maps for testing, you can
use the parameters below - but be warned, as the inherent randomness can lead to
different difficulties even with the same settings.  I picked maps where my (not
very optimized) solver could handle 1000 queries in about 30 seconds.

- Archipelago is a 10 x 10 grid with the default settings.
- Catacombs is a 10 x 10 grid with the default settings.
- Continents is a 6 x 6 grid with a scale (`-s`) of three.
- Ocean Maze is a 100 x 100 `water-maze` with 2 islands.
- Swiss Cheese is a 6 x 6 grid with the default settings.

In the Archipelago and Swiss Cheese maps, you always start on a bomb.


## `querygen.py`

This script  generates a bunch of queries  in the format used by the autograder:
one query (four integers) per line, separated by whitespace. It takes a map file
as a command line argument, and supports a few options.

- Use `-n` to control how many queries are generated.  The default is ten.
- Use `-s` and `-d` to control which map characters can be chosen as starting
  points and destinations, respectively.  The defaults are `.*` and `.*#`.


## `validate.py`

This script validates routes, similar to what the autograder does. By default it
runs in "interactive mode" and the user  has to enter the source and destination
points.  Use the `-q` option to have it read queries from a file instead.

If you're  using a query file  and  redirecting a route file  to the validator's
standard input, you can use the `-n` option to disable the interactive prompts.
