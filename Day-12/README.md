# Day 12 — Number Guessing Game

## What I built

A number guessing game with two difficulty levels : easy (10 attempts),
and hard (5 attempts). Python picks a random number, you guess,
it tells you higher or lower, and the clock is ticking.
First project using constants and a cleanly structured multi-function design.

## What I actually learned

### Constants

Variables written in ALL_CAPS signal that their value should never change:

```python
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
```

Not enforced by Python - it's a convention.
But conventions matter when others (or us in future) read our code.

### Functions that return values to control flow

`check_answer()` returns the updated turn count,
which gets passed back into the game loop:

```python
turns = check_answer(guess, answer, turns)
```

The function does one job, it checks the guess and return remaining turns.
The game loop decides what to do with that number.

### `return` inside a function

Using `return` mid-function exits it immediately -
used here to stop the game when turns run out:

```python
if turns == 0:
    print("You've run out of guesses. You lose.")
    return
```

No extra flags, no extra conditions. Just stop.

### `random.randint()`

Returns a random integer between two values, inclusive:

```python
answer = random.randint(1, 100)
```

Both 1 and 100 are possible - unlike `range()` which excludes the end.

### `while` loop with multiple exit conditions

The loop runs until the guess matches the answer,
but it also exits early if turns hit zero:

```python
while guess != answer:
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        return
```

Two ways out of the loop - win or lose.

### Importing specific items from a module

Instead of importing the whole module, we can import just what we need:

```python
from art import logo
```

Then use `logo` directly instead of `art.logo`.

## Project structure

Day-12/
├── art.py ← ASCII logo
├── number_guessing_game.py ← main game logic
└── README.md

## Reflection

The indentation bugs in this one were a good lesson -
Python doesn't just prefer clean indentation, it _requires_ it.
One misplaced line and the entire loop logic breaks silently
or crashes loudly.

Also learned the difference between `return` as an exit
vs `return value` as output. Small distinction, big impact.

On to Day 13.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
