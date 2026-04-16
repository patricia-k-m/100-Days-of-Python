# Day 04 — Rock Paper Scissors

## What I built

The classic hand game - against a computer that picks randomly.
You type a number, the computer picks its move and Python decides
who wins.
Simple game, but it introduces some very useful tools in Python.

## What I actually learned

### The `random` module

Python can't _actually_ be random - but the `random` module gets close enough.
`random.randint(0, 2)` returns a random whole number between 0 and 2, inclusive.

```python
import random
computer_choice = random.randint(0, 2)
```

Has to be `import`(ed) it first - it's not available by default.
This was my first time using a module. More of these are coming.

### Lists

A list is an ordered collection of items, stored in one variable.

```python
choices = [rock, paper, scissors]
```

Zero-based indexing - items sit in slots numbered from 0, not 1.

### Indexing — accessing items by position

Square brackets let us grab a specific item from a list by its position:

```python
choices[0]  # rock
choices[1]  # paper
choices[2]  # scissors
```

This is how the game connects the user's number input to the right ASCII image.

### IndexError

If we try to access a position that doesn't exist in the list,
Python throws an `IndexError`. That's why the code guards against it:

```python
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
```

### Nested lists

A list can contain other lists:

```python
nested = [[1, 2, 3], [4, 5, 6]]
nested[0][1]  # returns 2
```

## The project

```python
import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choice >= 0 and user_choice <= 2:
    print(choices[user_choice])

computer_choice = random.randint(0, 2)
print("(Computer chose: ")
print(choices[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("It's a draw!")
```

## Reflection

This was the first day that felt like a _real_ program.
Not just answering questions or following a path -
actual logic, actual randomness, actual game mechanics.

Code is Angela Yu's from the course walkthrough.
Concepts are understood, not just copied.

On to Day 05.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_

PUSŠ ZA COMMIT. OBAVEZNO OBRISATI SVE OVO DOLJE!!!!
git add .
git commit -m "Day 04: Rock Paper Scissors – random module, lists, indexing"
git push origin main

| [Day 04](./Day-04) | Rock Paper Scissors | Random module, lists, indexing, IndexError | # dodati u glavni read me
