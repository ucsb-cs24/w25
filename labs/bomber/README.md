# Bomber

In this lab,  you'll write a program  that can find routes  through an ASCII map
(the  atlas kind,  not the  `std::map` kind).  The map is fairly  standard, with
flat ground (`.`), walls (`#`), and water (`~`).  But  there are also some bombs
(`*`) laying around!  And if you find these,  you can use them  to blow up walls
and reach places that you wouldn't otherwise be able to...


## Your Assignment

Note that this is a challenge lab, so the rules are a little different!

- Implement the program described below.
- You may use anything from the standard library.
- You may work with a partner  if you choose to.  When submitting to Gradescope,
  put both partners' names on your final submission.
- The five fastest submissions get 50/40/30/20/10 points of extra credit.


## The Program

Your program should take  one command line argument.  This will be the path to a
map file,  as described below.  Your program  should then read  routing requests
from its standard input.  Each request will consist of four `int`s:

- The latitude of the starting point.
- The longitude of the starting point.
- The latitude of the destination.
- The longitude of the destination.

Your program should then attempt to find a route from the starting point to the
destination, and print a single line with the result:

- If either point is invalid, print a line starting with `Invalid`.
- If there is no possible route, print a line starting with `No route`.
- Otherwise, print the route as described below.

Keep reading routing requests and printing routes until you reach the end of the
input.  Then exit.

```
[ariadne@naxos]$ cat data/map.txt
...#..
.*.###
......
###.##
.....#
[ariadne@naxos]$ ./bomber data/map.txt
src> 0 0
dst> 4 0
eessesswww
src> 4 0
dst> 0 4
eeennwwnneeee
src> 0 4
dst> 4 0
No route from (0, 4) to (4, 0).
```

The skeleton in `main.cpp` is a good place to start,  although you're welcome to
change it as long as your program still behaves as specified above.  If you want
to use the pre-built `main()` function, implement the following `Map` functions.

- The constructor should take an input stream and read in a map file.
- Add a destructor if your `Map` needs to clean up any external resources.
- The `route()` function should try to find a route between two points:
  - If either input point is invalid, throw a `PointError`.
  - If there is no possible route, throw a `RouteError`.
  - Otherwise, return a valid route as a string.


### Map Files

A map is just a text file.  All the lines in the file will be the same length,
and will contain only the following characters (and newline characters).

- `.`  This is regular ground.  You can walk on it.
- `*`  This is a bomb sitting on regular ground.  If you walk on it, you pick up
  the bomb and the space becomes regular ground (`.`).
- `#`  This is a boulder.  If you  aren't carrying any bombs,  you can't walk on
  it. If you're carrying at least one bomb, you _can_ walk onto it: this uses up
  one bomb to destroy the boulder and the square becomes regular ground (`.`).
- `~`  This is water.  You can't walk on it.

### Routes

A route is simply a string  that describes where to go.  To follow a route, loop
over the characters in the string and move accordingly:

- `n`  Move one square north.
- `e`  Move one square east.
- `s`  Move one square south.
- `w`  Move one square west.

All other characters are invalid.

### Coordinates

The first line of a map file is the north edge; the last line is the south edge.
The first character of each line  is the westernmost,  and the last character of
each line is the easternmost.

The northernmost edge of the map is at latitude zero;  latitude increases as you
move  south.  The westernmost  edge of the map  is at longitude zero;  longitude
increases as you move east.

When entering or displaying points, latitude comes before longitude.

### Extra Details

- A starting point is invalid if its coordinates are out of bounds, or if you
  can't walk on the terrain at that point.
- A destination point is only invalid if its coordinates are out of bounds.
- You always start without any bombs.
- If you start on a square with a bomb, you immediately pick it up.
- All  routes are for the  original map.  Any changes  you make to the map while
  calculating one route need to be reset before calculating the next route.


## Hints

- Make it work first.  Make it fast later.
- You can return any valid route.  It doesn't have to be the shortest route.
- The performance tests will run lots of route queries per map.  If you can save
  time in your  routing function  by doing more work  in your constructor,  it's
  probably worth it.
- When compiling your code for the performance tests, the autograder will add
  the `-O3` flag to enable extra compiler optimizations.
- The autograder will always run your program with exactly one command line
  argument, which will be a valid path to a valid map file.
