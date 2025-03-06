#ifndef MAP_H
#define MAP_H

#include <iostream>
#include <string>

#include "Point.h"


class Map {
    // Member Variables

public:
    Map(std::istream& stream);
    // ~Map();

    std::string route(Point src, Point dst);
};

#endif
