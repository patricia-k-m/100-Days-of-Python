# Day 10 — Calculator

## What I built

A fully functional calculator that can add, subtract, multiply, divide.
After each calculation you can keep going with the result,
or start fresh. Built with functions stored inside a dictionary
and recursion to restart cleanly.

## What I actually learned

### Functions as first-class objects

In Python, functions can be stored in variables, lists, and dictionaries.
This project uses that to map operator symbols directly to functions:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

No `if/elif` chain needed. Just look up the symbol and call whatever's there:

```python
answer = operations[operation_symbol](num1, num2)
```

### Dictionary of functions

`operations[operation_symbol]` returns the function itself.
Adding `(num1, num2)` immediately calls it with those arguments.
Clean, scalable, and satisfying to write.

### Accumulating results

Instead of starting fresh every time, the result becomes the next `num1`:

```python
if choice == "y":
    num1 = answer
```

This is what makes it feel like a real calculator -
you can actually chain operations: `2 + 3 * 4 / 2`...

### Recursion

When the user wants to start over, the calculator calls itself:

```python
else:
    should_accumulate = False
    print("\n" * 20)
    calculator()
```

This is recursion, a function that calls itself.
It restarts the whole flow cleanly without a messy reset loop.

### `while` loop with a flag

`should_accumulate` keeps the calculation going until
the user decides to stop:

```python
should_accumulate = True
while should_accumulate:
    # calculate
    if choice == "y":
        num1 = answer
    else:
        should_accumulate = False
```

### Looping through a dictionary to display options

```python
for symbol in operations:
    print(symbol)
```

Iterating over a dictionary gives us its keys or
in this case the operator symbols `+`, `-`, `*`, `/`.

## Project structure

Day-10/
├── art.py ← calculator ASCII logo
├── calculator.py ← main calculator logic
└── README.md

## Reflection

The `operations` dictionary was the moment this day clicked.
Storing functions as values, and not just strings or numbers,
changes how you think about what a dictionary can do.

Also: recursion. It sounds intimidating.
In practice it's just a function saying "start me over."
Simple concept, powerful tool.

On to Day 11.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
