# Day 09 — Secret Auction

## What I built

A secret auction program : multiple bidders enter their name and bid
privately, the screen clears between each bidder, and at the end
Python reveals the winner with the highest bid.
First real use of dictionaries to store and process structured data.

## What I actually learned

### Dictionaries

A dictionary stores data as key-value pairs.
In this project, each bidder's name is the key and their bid is the value:

```python
bids = {}
bids[name] = price
```

Unlike lists which use numbered indexes, dictionaries use meaningful keys.
`bids["Patricia"]` is clearer than `bids[0]`.

### Iterating over a dictionary

We can loop through a dictionary just like a list.
Each iteration gives us a key:

```python
for bidder in bidding_dictionary:
    bid_amount = bidding_dictionary[bidder]
```

`bidder` is the name, `bidding_dictionary[bidder]` is their bid amount.

### Passing a dictionary to a function

The entire `bids` dictionary gets passed into `find_highest_bidder()`
as one argument so there's no need to pass each value separately:

```python
find_highest_bidder(bids)
```

### Finding the highest value manually

Instead of using a built-in, the logic tracks the winner by
comparing each bid to the current highest:

```python
if bid_amount > highest_bid:
    highest_bid = bid_amount
    winner = bidder
```

Simple, readable, and shows exactly what's happening under the hood.

### Clearing the screen with `print("\n" * 100)`

Between bidders, the screen gets flooded with blank lines
so no one can scroll up and see previous bids:

```python
print("\n" * 100)
```

Not a real clear — but effective enough for a terminal program.

### Boolean flags

`continue_bidding` controls the auction loop.
One small but important lesson(for me): `False` and `"False"` are not the same thing.
`"False"` is a non-empty string - it's truthy.
`False` is the actual boolean - it stops the loop.

```python
continue_bidding = False  # correct
continue_bidding = "False"  # wrong - loop never ends
```

## Project structure

Day-09/
├── art.py ← auction house ASCII logo
├── README.md
└── secret_auction.py ← main auction logic

## Reflection

Dictionaries clicked today. The idea of storing related data
as named pairs (not just a numbered list) opens up a whole
new way of thinking about data structure.

Also caught a real bug in my own code: `"False"` vs `False`.
One character of difference, completely different behavior.
That's the kind of thing you only learn by making the mistake.

On to Day 10.

---

_Part of my [100 Days of Python](../) journey · Angela Yu's 100 Days of Code Bootcamp_
