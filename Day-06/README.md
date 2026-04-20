# Day 06 — Reeborg's World

## What I built

Five solutions for Reeborg's World - a browser-based Python puzzle environment
where you control a robot by writing real Python code. No print statements,
no input() — just logic, loops and functions that make something _move_.

- **Hurdle 1** - jump over 6 hurdles using a for loop
- **Hurdle 2** - jump until goal using a while loop
- **Hurdle 3** - variable hurdle positions, nested while loops
- **Hurdle 4** - variable hurdle _heights_, the most complex jump logic
- **Maze** - navigate any maze using the right-hand rule algorithm

## What I actually learned

### Functions

A function is a reusable block of code you define once and call many times.
Day 06 was the first day where functions weren't optional, they were necessary.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```

Reeborg only knows `turn_left()`, so `turn_right()` had to be built
from scratch. Three left turns = one right turn. Simple and satisfying.

### `for` loops with `range()`

Used in Hurdle 1 to jump exactly 6 times:

```python
for i in range(times):
    running_jump()
```

### `while` loops

Used when we don't know how many times to repeat - just _until_ something is true:

```python
while not at_goal():
    running_jump()
```

### Nested `while` loops

Hurdle 3 and 4 use loops inside loops - move forward while you can,
then jump when you hit a wall:

```python
while not at_goal():
    while front_is_clear():
        move()
    jump()
```

### Conditionals inside loops

The maze solution combines `while`, `if`, and `elif` into one clean algorithm:

```python
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

This is the **right-hand rule**, a classic maze-solving algorithm.
Keep your right side to the wall and you'll always find the exit.

### `wall_on_right()`, `front_is_clear()`, `at_goal()`

Reeborg's built-in condition checkers - these are what make
the robot _aware_ of its environment. They return `True` or `False`,
which plugs directly into `if` and `while` conditions.

## Reflection

This was the first day that felt like _problem solving_ rather than
just following syntax. Especially Hurdle 4 and the Maze -
there's no single right answer, just logic that either works or doesn't.

The maze solution is 7 lines. It solves every maze variation.
That ratio of simplicity to power is what I want more of.

Since Reeborg runs in the browser, the code lives in `.txt` files here
with copy-paste instructions at the top.

On to Day 07.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
