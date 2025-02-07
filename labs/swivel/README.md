# Swivel

In this  lab,  you'll implement the  _set_  abstract data type  using a  _binary
search tree_ as the  concrete data type.  The set will store `std::string`s  and
order them asciibetically:  all the values in a node's left subtree will be less
than the value stored in that node, and all the values in the right subtree will
be greater.

This tree is  _not_ necessarily balanced.  There will be cases where it has poor
(O(n)) performance.

Run `git pull upstream master` in your Git repo to get the starter code.


## Your Assignment

- Implement a set in the `.h` and `.cpp` files provided:
  - Declare a binary tree node type called `Node` in `Node.h`.
  - Implement any `Node` member functions (or helper functions) in `Node.cpp`.
  - Implement the `Set` member functions declared in `Set.h` in `Set.cpp`.
- You can't use any [container classes][containers] from the standard library.
- Make sure your final code doesn't print anything unexpected.
- Make sure you don't have any memory leaks.


## Functions

Implement the following `Set` member functions  in `Set.cpp`.  Most of these are
standard set operations, but this set also has a special operation called swivel
that can bring any value up to be the root of the tree.

- The default constructor creates an empty set.
- The copy constructor creates a copy of an existing set.
- The move constructor takes the nodes from a set that's about to be deleted.
- The destructor deletes all the nodes in the set.
- `clear()` removes all the values from the set. It returns the number of values
  that were removed.
- `contains(value)` checks if a value is present in the set.
- `count()` returns the total number of values in the set.
- `debug()` does whatever you want it to.  Implement this if you want some other
  output when testing locally; otherwise ignore it.  This function isn't tested.
- `insert(value)` adds a value  to the set.  If the value is already present, it
  does nothing.  It returns the number of values that were added.
- `print()`  prints the structure of the set in tree notation, as defined below,
  followed by a single newline.
- `swivel(value)` behaves like `contains()`  in that it returns whether or not a
  value is in the set. But it also modifies the tree: if the value is present in
  the set, the node holding the value swivels up repeatedly (see below) until it
  become the root. If the value isn't present, the last node it searched swivels
  up instead.
- `remove(value)` removes a value from the set  and returns the number of values
  that were removed.  Implement it with `swivel()`:
  - First, call `swivel()` on the value to be removed.
  - If the value wasn't found, stop here.  Otherwise, the value to remove is now
    the root of the tree.
  - If the value to remove is on a node with less than two children, remove that
    node.  If the node had a child, the child becomes the new root.
  - If the value is on a node with two children, removing it will leave you with
    two "subtrees."  The left subtree will contain values smaller than the value
    that was removed, and the right subtree will contain greater values.  Swivel
    the smallest value in the right subtree up  to become the root.  Afterwards,
    it will not have a left child; attach the left subtree as its left child.


## Swiveling

In a binary tree,  a parent-child link can "swivel," or rotate.  The result is a
new layout for the binary tree.  The search tree ordering  is preserved, but the
old child node is now the parent, and the old parent is now the child:

```
    d           b
   / \         / \
  b   e  <=>  a   d
 / \             / \
a   c           c   e
```

Note that when nodes `b` and `d` swivel, node `c`'s parent changes as well!

Any node in the tree can become the root  by swiveling up repeatedly.  Node `c`,
for example, could become the root after swiveling up twice:

```
    d          d          c
   / \        / \        / \
  b   e  =>  c   e  =>  b   d
 / \        /          /     \
a   c      b          a       e
          /
         a
```


## Tree Notation

A binary tree might look something like this:

```
    d
   / \
  b   e
 / \   \
a   c   f
```

But we need an easy way  to print a tree to the console.  So we'll define a tree
notation that lets us write a tree structure as a single line. In this notation,
the tree pictured above would look like this:

```
((a b c) d (- e f))
```

More formally:
- The tree notation for a leaf node is simply its value.
- The tree notation for a non-existent node is a hyphen (`-`; ASCII value 45).
- The tree notation for a non-leaf node is:
  - A left parenthesis, followed by
  - the tree notation for its left subtree, followed by
  - a space, followed by
  - the node's value, followed by
  - a space, followed by
  - the tree notation for its right subtree, followed by
  - a right parenthesis.
- The tree notation for an empty tree is `-`.


## Hints

- Recursion works even better with trees than it does with linked lists.
- The standard string comparison operators will give you the correct ordering.
- The `insert()` and `remove()` functions will always return one or zero.
- The `swivel()` function only looks at one node at each level in the tree, just
  like like `contains()`.  If the value to swivel isn't present,  the "last node
  searched" will have at least one null child.
- You'll need at least a default constructor, `insert()`, and `print()` before
  you can pass any tests on Gradescope.


[containers]: https://cplusplus.com/reference/stl/
