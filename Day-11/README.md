# Day 11 — Blackjack

## What I built

A fully playable Blackjack game in the terminal - deal cards,
calculate scores, handle Aces, let the computer play, and find out
who wins. The most complex project so far, and the first one
that required real upfront planning before writing a single line.

## What I actually learned

### Functions that return values

Every major piece of logic lives in its own function,
and each function returns something useful:

```python
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
```

`deal_card()` doesn't print, it returns.
The result gets stored and used elsewhere.
That separation of concerns is what keeps the code readable.

### `sum()` and `len()`

Two built-ins that do heavy lifting here:

```python
if sum(cards) == 21 and len(cards) == 2:
    return 0  # blackjack
```

`sum()` adds up all values in a list.
`len()` counts the items. Together they check for blackjack
in one clean condition.

### Handling the Ace - `list.remove()` and `list.append()`

The Ace is 11 by default. If it pushes the score over 21,
it becomes 1:

```python
if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
```

`remove()` deletes the first matching value.
`append()` adds the replacement. Elegant solution to a tricky rule.

### Using 0 as a special return value

Blackjack (Ace + 10 in two cards) returns `0` instead of `21`.
This lets the `compare()` function treat it as a special case
without needing extra flags:

```python
if user_score == 0:
    return "Win with a Blackjack."
```

A simple convention that avoids a lot of complexity.

### `compare()` - layered conditionals

The compare function works through every possible outcome
in priority order — both bust, draw, blackjacks, busts, then score comparison:

```python
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    # ...and so on
```

Order matters here. The bug fix at the top (both over 21)
has to come first or the logic breaks.

### Computer AI with a `while` loop

The computer keeps drawing until it hits 17 or above:

```python
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
```

Simple rule, realistic behavior. This is how real casino
dealers are required to play.

### `for _ in range(2)` - deal two cards

The underscore `_` is used when you need to loop
but don't care about the loop variable:

```python
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
```

"Pythonic" and clean.

### Restarting with a `while` loop

```python
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
```

The condition is evaluated every time -
if the user types `'y'`, the game runs. Anything else, it stops.

## Project structure

Day-11/
├── art.py ← Blackjack ASCII logo
├── blackjack_game.py ← main game logic with Angela's hints preserved
└── README.md

## Reflection

This was the first project that needed a lot of planning before code.
Three separate functions, each doing one job, all connected through
a `play_game()` orchestrator.

The Ace handling was the trickiest part - a card that changes its
own value based on context.
`remove()` and `append()` solved it in two lines.

Angela Yu's hints are kept in the file intentionally this time.
They show how to break a complex problem into steps - that thinking
process is worth documenting.
This project took more time than I expected, but it was rewarding.

On to Day 12.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
