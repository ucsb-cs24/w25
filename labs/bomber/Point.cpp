#include "Point.h"

std::ostream& operator << (std::ostream& stream, const Point& point) {
  return stream << '(' << point.lat << ", " << point.lng << ')';
}

std::istream& operator >> (std::istream& stream, Point& point) {
  return stream >> point.lat >> point.lng;
}
