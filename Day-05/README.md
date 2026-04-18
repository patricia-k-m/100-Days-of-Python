# Day 05 — Password Generator

## What I built

A password generator that asks how many letters, symbols, and numbers
you want and then shuffles them into a random, secure password.
Two solutions in one file: an easy version (commented out) and
a harder, better one. Both work. One is a bit advanced (or smarter).

## What I actually learned

### `for` loops

A `for` loop repeats an action a set number of times.
`range(0, nr_letters)` runs the loop exactly `nr_letters` times.

```python
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
```

### `random.choice()`

Picks a random item from a list. Used here to grab a random
letter, symbol, or number each time the loop runs.

```python
random.choice(letters)
```

### `list.append()`

Adds an item to the end of a list.

```python
password_list.append(random.choice(letters))
```

### `random.shuffle()`

Shuffles a list in place and reorders its items randomly.
This is what makes the password truly random instead of
always being letters first, then symbols, then numbers.

```python
random.shuffle(password_list)
```

### Easy vs Hard solution

The easy solution builds the password as a string directly:

```python
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
```

The hard solution builds a list first, shuffles it,
then joins it into a string. The shuffle is what makes it harder
and what makes the password actually secure.

### Joining a list into a string

Python can't print a list as a clean password,
so it loops through it and builds a string:

```python
password = ""
for char in password_list:
    password += char
```

## Reflection

This was the first day where I wrote two solutions to the same problem -
and understood why one is better than the other.
The easy version works. The hard version is _correct_.
That distinction is starting to matter to me.

On to Day 06.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
