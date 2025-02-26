"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    # Use string replace for each emoticon
    return txt.replace('smile', ':D').replace('grin', ':)').replace('sad', ':(').replace('mad', ':P')

    # alternate solutions:
    # create a dictionary, separate the string to a word list and reconstruct it with the emoticons by using the dictionary to look up the last word

    # create a dictionary and do the chaining above but with a for loop (helpful for a more involved replacement scheme)

    # ... many other ways

