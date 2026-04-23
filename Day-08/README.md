# Day 08 — Caesar Cipher

## What I built

The Caesar Cipher is one of the oldest encryption techniques in history.
You type a message, pick a shift number, and every letter shifts
that many positions through the alphabet. Run it again to decode.
This project truly feels like something you'd actually use.

## What I actually learned

### Functions with multiple parameters

The `caesar()` function takes three arguments - text, shift, and direction.
Clean, reusable, and called the same way every time:

```python
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
```

Using keyword arguments makes the function call self-documenting so
we know exactly what each value is for just by reading it.

### Modulo operator `%`

The secret weapon of this project. When the shift goes past `z`,
it wraps back around to the start of the alphabet:

```python
shifted_position %= len(alphabet)
```

Without this, shifting `'z'` by 1 would crash. With it,
we get `'a'`.

### `list.index()`

Finds the position of an item in a list:

```python
shifted_position = alphabet.index(letter) + shift_amount
```

This is how the cipher finds where a letter sits,
shifts it, and picks the new letter at that position.

### Handling non-alphabet characters

Spaces, numbers, punctuation pass through untouched:

```python
if letter not in alphabet:
    output_text += letter
```

Encoded message keeps its spaces and symbols.
Only letters get encrypted.

### Encode vs decode in one function

Instead of two separate functions, one handles both directions:

```python
if encode_or_decode == "decode":
    shift_amount *= -1
```

Decoding is just encoding in reverse. Multiply the shift by `-1`
and the same logic works both ways.

### `while` loop as a game loop with a flag

`should_continue` controls whether the program keeps running:

```python
should_continue = True

while should_continue:
    # run the cipher
    if restart == "no":
        should_continue = False
```

Cleaner than `break` - the flag makes the exit condition explicit.

### Importing from a separate file

Like Day 07, the logo lives in its own file:

```python
import art
print(art.logo)
```

## Project structure

Day-08/
├── art.py ← Caesar Cipher ASCII logo
├── caesar.py ← main cipher logic
└── README.md

## Reflection

This one connected history to code. Caesar actually used this cipher
to protect military messages. The math behind it - modulo arithmetic,
wrapping around an alphabet - is the same math behind modern cryptography.

It's a toy cipher. But the thinking behind it is surely not.

On to Day 09.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
