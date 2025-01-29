# Assort

In this lab, you'll implement a sorted sequence using a singly-linked list.  The
sequence will store strings in "asciibetical" order.

An "asciibetical" sort is a very simple sort.  It sorts strings according to the
[ASCII values][ascii] of their individual `char`s. It doesn't always do what you
would expect -- it puts capital letters  before lower case letters,  and doesn't
really work for languages that use multi-byte characters -- but it's good enough
for this lab.  Just use the standard string  comparison operators and you'll get
the correct ordering.


## Your Assignment

- Implement the linked list declared in `List.h`.
- Store values in ascending asciibetical order (`A` before `Z` before `a`).
- You can't use any [container classes][containers] from the standard library.
- Make sure your final code doesn't print anything.
- Make sure you don't have any memory leaks.


## Functions

Implement the following `List` member functions  in `List.cpp`.  You can add any
helper functions you need,  but they can't be member functions of the `List` and
`Node` classes (since they aren't declared in `List.h`).

- The default constructor creates an empty list.
- The copy constructor makes a copy of an existing list.
<!-- - The move constructor takes the values from a list that's about to be deleted. -->
- The destructor cleans up the list.
- `count()`  Get the number of values in the list.
- `insert(value)`  Insert `value` at its correct position in the list.
- `lookup(index)`  Get the value stored at `index`. If `index` is invalid, throw
  a `std::out_of_range` exception.
- `print(reverse)`  Print the values stored in the list.  Separate values with a
  comma and a space.  Enclose your output in square brackets and print a newline
  after the closing bracket. If `reverse` is false (the default), print the list
  in it's natural (ascending) order:
  ```
  [Atropos, Clotho, Lachesis]
  ```
  If `reverse` is true, print it in descending order:
  ```
  [Lachesis, Clotho, Atropos]
  ```
- `remove(index)`  Remove the value stored at `index` and return it.  If `index`
  is invalid, throw a `std::out_of_range` exception.
- `remove(value)`  Remove all copies of `value` from the list. Return the number
  of values that you removed.


## Hints

- Recursion works very nicely on linked lists.
- Work on the `insert()` and `print()` (forward) functions first. These are used
  in almost all the tests, so you won't pass much until they work.
- Don't write a `main()` function in `List.cpp`.  If you want to test your code,
  use the `main()` function in `test.cpp` (or some other new `.cpp` file).


[ascii]: https://xavierholt.github.io/cheatsheets/ascii.html
[containers]: https://cplusplus.com/reference/stl/
