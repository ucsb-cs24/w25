#ifndef ERRORS_H
#define ERRORS_H

#include "Point.h"

struct PointError {
  Point point;

  PointError(const Point& point): point(point) {
    // All done.
  }
};

struct RouteError {
  Point src;
  Point dst;

  RouteError(const Point& src, const Point& dst): src(src), dst(dst) {
    // All done.
  }
};

#endif
