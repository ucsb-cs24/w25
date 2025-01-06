# Syllabus

## Overview

This is a class about data structures.  You learned the basics of coding in your
previous CS classes;  now we'll talk about  how your data  is laid out in memory
and  how to organize it efficiently.  We'll talk about  abstract data structures
like sequences,  heaps,  sets,  and maps;  the concrete data structures  used to
implement them, like vectors, binary trees, and hash tables;  the performance of
the concrete implementations; and how to use these structures to solve problems.

This is also a C++ class, but we won't focus too much on C++ syntax. You'll pick
that up for yourself as you do the programming assignments. Come to lab sections
or ask on Piazza if you have language questions!


## Materials

Everything in this class is optional except  the programming assignments and the
quizzes.  I don't take attendance.  Lecture notes will be available on GitHub or
on Piazza.  There is no  required reading.  There is no textbook.  Everything we
talk about in this class is common computer science  material,  and you can find
it online in whatever format you like best.  If you like having a textbook, here
are some possibilities:

- **Data Structures and Other Objects Using C++** by Michael Main and Walter Savitch\
  This used to be the standard textbook for other CS 24 courses.
- **Problem Solving with C++** by Walter Savitch\
  This is an optional textbook for other CS 24 courses.
- **Data Structures and Algorithm Analysis in C++** by Mark Allen Weiss\
  This is the standard textbook for CS 130A.


## Grading

Your grade comes from two sources:

- **Programming Assignments**  There will be about eight of these, one per week,
  all  (roughly)  equally weighted.  You can turn these in up to four days late,
  but at a penalty of  ten percent per day:  an assignment due on Tuesday can be
  turned in on Wednesday for 90% of  your Gradescope score,  on Thursday for 80%
  of your score, and so on; it cannot be turned in on Sunday.

- **Quizzes**  There will be three of these,  or about one per month.  They will
  take place during regular lecture time. A typical quiz will ask you to write a
  function or a short program with pen and paper.

Your final score  will be a combination of your scores  on these two components.
This will likely _not_ be a simple weighted average; this is my first time using
quizzes in CS 24, so I'm not sure what the optimal combination function will be.
For a rough estimate, multiply your scores together and take the square root.

If you get at least 90% of the available points on both components (separately),
you are guaranteed  at least an A-,  getting 80% of the points guarantees you at
least a B-, 70% a C-, and so on.


## Coding

This is a C++ class,  so you'll be coding in C++.  We'll be using C++ 17 (C++ 23
is the latest standard),  so compile your code with the `-std=c++17` flag.  Your
code must compile with no warnings.  Use the `-Wall`,  `-Wextra`,  and `-Werror`
flags  to enforce this.  The full compilation command also enables debug symbols
and allows unused function arguments (to make stubbing less painful):

```sh
g++ -std=c++17 -g -Wall -Wextra -Werror -Wno-unused-parameter ...
```

Your code must also run without any memory errors: things like memory leaks, use
of uninitialized variables, out-of-bounds reads or writes, etc.  To ensure this,
the autograder will run your programs  in Valgrind, a memory error detector.  To
replicate this, use the following command (Linux-only, but should work in WSL):

```sh
valgrind --leak-check=full -- ./myprogram arg1 arg2 ...
```

These commands  can be a bit verbose;  you are encouraged to write Makefiles and
save yourself some typing.

Your assignments will be  auto-graded on Gradescope,  which is currently running
GCC 11.4.0 in Ubuntu 22.04 containers.  Code written on other platforms may need
slight tweaking to compile correctly on Gradescope. In particular, Mac users may
need to include more header files.


## Piazza

We'll be using Piazza as a Q&A forum. If you have a question that might apply to
other people as well, it's better to ask on Piazza than to send an email.

If you ask coding questions on Piazza, please:

- Post the smallest section of code that fully describes your problem.
- Include any code as a code snippet.  Not a screenshot. Not a cell phone photo.
- In Markdown mode, use triple backticks (`` ``` ``) to format code blocks.
- If you include more than a few lines of your code, make your question private.


## Cheating

All assignments are individual assignments. Write your own code.  You're welcome
(encouraged, even!)  to talk about the assignments with your classmates, but you
should be able to discuss everything we do without ever sharing any code.

All work you submit must be your own work. If you choose to ignore this and turn
in code written by  a person  (or computer)  that is not you,  remember that the
following penalties apply to all parties involved:

- **First Offense:** Zero on the assignment _and_ final grade lowered by one letter.
- **Second Offense:** Fail the class.

The programming assignments  are involved enough  that it's virtually impossible
for anyone to have the same code as you  by accident.  As long as you write your
own code you have nothing to worry about.
