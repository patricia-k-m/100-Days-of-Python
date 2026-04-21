# Day 07 — Hangman

## What I built

The classic Hangman game - Python picks a random word, you guess letters
one at a time, and you have 6 lives before the hangman is complete.
First multi-file project: logic, art, and data all separated into their own files.

## What I actually learned

### Importing from multiple files

Day 07 was the first project split across multiple files.
Instead of one big script, everything has its place:

```python
from hangman_words import word_list
from hangman_art import stages, logo
```

`hangman.py` is the brain. `hangman_art.py` is the display.
`hangman_words.py` is the data. Clean separation for cleaner thinking.

### `for` loops over strings

You can loop through a string letter by letter, just like a list:

```python
for letter in chosen_word:
    if letter == guess:
        display += letter
```

### Building a display string dynamically

Each guess updates what the player sees - revealed letters stay,
unknown ones stay as `_`:

```python
for letter in chosen_word:
    if letter == guess:
        display += letter
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"
```

### Tracking state with a list

`correct_letters` keeps a running record of every correct guess,
so previously revealed letters don't disappear on the next turn:

```python
correct_letters = []
correct_letters.append(guess)
```

### `while` loop as a game loop

The entire game runs inside a `while` loop that keeps going
until `game_over` is set to `True`:

```python
game_over = False
while not game_over:
    # game logic here
```

### Lives and indexed stages

`lives` starts at 6 and counts down with each wrong guess:

```python
lives -= 1
```

`stages[lives]` uses the current lives count as an index -
as lives drop, the hangman builds up.

### f-strings for dynamic messages

```python
print(f"********************{lives}/6 LIVES LEFT ********************")
print(f"It was {chosen_word}! You lose.")
```

## Project structure

Day-07/
├── hangman_art.py ← ASCII art stages and logo
├── hangman_game.py ← main game logic
├── hangman_words.py ← word list
└── README.md

## Reflection

This was the biggest project so far. Not because the code is complex,
but because it required thinking about _structure_.
Three files, each doing one job. That's not just good Python,
that's good programming in any language.

Also: watching the hangman build up as lives drop never gets old.

On to Day 08.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
