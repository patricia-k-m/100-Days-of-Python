# Day 03 — Treasure Island

## What I built

A text-based adventure game. You're at a crossroads, you make choices,
and those choices lead to treasure or death. Classic.
The code is largely Angela Yu's from the course walkthrough.
I modified some of the dialogue to make it my own.
The logic, structure, and concepts - those I followed and understood.

## What I actually learned

### Conditionals - `if`, `elif`, `else`

The backbone of decision-making in Python.
If this is true, do this. Otherwise, check this. Otherwise, do that.

```python
if choice1 == "left":
    # something happens
elif choice1 == "right":
    # something else
else:
    # fallback
```

### Nested `if` statements

Decisions inside decisions. This is where the game gets its branching paths.
Each choice opens a new set of conditions.

```python
if choice1 == "left":
    if choice2 == "wait":
        if choice3 == "yellow":
            print("You win!")
```

The indentation is everything here. Python uses it to know what belongs to what.

### `.lower()`

Makes user input case-insensitive. If someone types "Left" or "LEFT",
it still matches "left". Small detail, big usability difference.

```python
choice1 = input("Left or right? ").lower()
```

### Escape characters

When string contains a quote, we need to escape it with `\`
so Python doesn't think the string ended early.

```python
input('You\'re at the crossroad.')
```

## Reflection

This one was less about writing code and more about _reading_ it.
Following Angela Yu's logic, tracing each branch, understanding
why the indentation matters and what happens when you nest conditions
three levels deep.

I changed the dialogue a bit. Small thing, but it made it feel like mine.
Next time I want to try building a branching story from scratch.

On to Day 04.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
