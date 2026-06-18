# Day 13 — Debugging

## What this day was about

No new project today. Day 13 was about learning how to _find and fix_ bugs
which is a skill as important as writing code in the first place.
Three debugging exercises, five bugs total.

## Debugging techniques covered

### Describe the problem

Before touching the code, we say out loud what it should do vs. what it's doing.
The gap between those two things is where the bug lives.

### Play computer

Trace through the code manually, line by line, as if you were Python.
What is the value of each variable at each step?

### Use `print()` to inspect

When in doubt, print everything:

```python
print(f"number = {number}")
print(f"score = {score}")
```

Seeing actual values at runtime often reveals the bug immediately.

### Rubber duck debugging

Explain your code out loud to someone (or something) that can't respond.
The act of explaining forces you to slow down and see what's actually there.

---

## The exercises

### Exercise 1 - Odd or Even

**Bug:** `=` used instead of `==` in the condition.

```python
# Buggy
if number % 2 = 0:

# Fixed
if number % 2 == 0:
```

`=` assigns a value. `==` checks equality.
Python raises a `SyntaxError` here, which is one of the more helpful errors.

---

### Exercise 2 - Leap Year

**Bug:** `input()` returns a string. Modulo `%` needs an integer.

```python
# Buggy
year = input("Which year do you want to check?")

# Fixed
year = int(input("Which year do you want to check?"))
```

This is a `TypeError` - Python can't do `"2024" % 4`.
Always convert `input()` when you need a number.

---

### Exercise 3 - FizzBuzz

Three bugs in one exercise:

**Bug 1:** `print([number])` wraps the number in a list.

```python
# Buggy
print([number])

# Fixed
print(number)
```

**Bug 2:** `or` instead of `and` for the FizzBuzz condition.

```python
# Buggy - prints FizzBuzz when EITHER is divisible
if number % 3 == 0 or number % 5 == 0:

# Fixed - prints FizzBuzz only when BOTH are divisible
if number % 5 == 0 and number % 3 == 0:
```

**Bug 3:** Multiple `if` statements instead of `elif` -
multiple branches could fire for the same number.

```python
# Buggy - all three ifs checked independently
if number % 3 == 0:
if number % 5 == 0:

# Fixed - only one branch runs per number
elif number % 3 == 0:
elif number % 5 == 0:
```

---

## Reflection

Debugging is humbling. Three small exercises, five bugs total,
and each one required actually _reading_ the code.
Not skimming it, not assuming it was right.

The FizzBuzz exercise was the most interesting:
three separate bugs, each subtle, each breaking the output
in a different way. Finding all three required checking logic,
types, _and_ control flow.

Debugging isn't separate from coding. It _is_ coding.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
