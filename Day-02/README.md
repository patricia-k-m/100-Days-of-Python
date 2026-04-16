# Day 02 — Tip Calculator

## What I built

A Tip Calculator - asks for the bill total, tip percentage, and number of
people splitting it. Spits out exactly what each person owes.
I can see this actually being used in real life.

## What I learned

### Data types

Python cares what _kind_ of thing a value is. Day 01 was all strings.
Today I met the others:

| Type    | Example   | What it is     |
| ------- | --------- | -------------- |
| `str`   | `"hello"` | Text           |
| `int`   | `10`      | Whole number   |
| `float` | `10.5`    | Decimal number |

### Type conversion

`input()` always gives a string - even if the user types a number.
So it has to be converted manually:

```python
bill = float(input("What was the total bill? $"))
people = int(input("How many people? "))
```

`float()` for decimals, `int()` for whole numbers.

### f-strings

A cleaner way to drop variables into text. Instead of concatenating with `+`:

```python
# old way (how I would do it Day 01 style)
print("Each person pays: $" + str(final_amount))

# f-string way
print(f"Each person should pay: ${final_amount}")
```

The `f` before the quote tells Python: _variables incoming_.
Wrap the variable in `{}` and that's it.

### `round()`

`round(number, 2)` rounds to 2 decimal places — keeps the output
looking like actual money instead of `$12.666666667`.

```python
final_amount = round(bill_per_person, 2)
```

## The project

```python
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
```

## Reflection

Day 01 was "make Python talk." Day 02 is "make Python calculate."
The jump felt small but the concept is big - data has types,
and you have to be deliberate about them.
Coming from front-end where JavaScript jus figures it out,
this feels more honest somehow.

On to Day 03.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
