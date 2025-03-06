#include <fstream>
#include <iostream>

#include "Errors.h"
#include "Map.h"

int main(int argc, char** argv) {
  bool interactive = false;
  const char* filename;

  if(argc == 3 && std::string("-i") == argv[1]) {
    interactive = true;
    filename = argv[2];
  }
  else if(argc == 2) {
    filename = argv[1];
  }
  else {
    std::cerr << "USAGE: " << argv[0] << "[-i] map-file.txt\n";
    return 1;
  }

  std::ifstream stream(filename);
  if(stream.fail()) {
    std::cerr << "ERROR: Could not open file: " << filename << '\n';
    return 1;
  }

  Map map(stream);

  while(true) {
    Point src;
    Point dst;

    if(interactive) {
      std::cout << "src> ";
    }
    std::cin >> src;
    if(std::cin.fail()) {
      break;
    }

    if(interactive) {
      std::cout << "dst> ";
    }
    std::cin >> dst;
    if(std::cin.fail()) {
      break;
    }

    try {
      std::cout << map.route(src, dst) << '\n';
    }
    catch(const RouteError& e) {
      std::cout << "No route from " << e.src << " to " << e.dst << ".\n";
    }
    catch(const PointError& e) {
      std::cout << "Invalid point: " << e.point << '\n';
    }
  }

  return 0;
}
