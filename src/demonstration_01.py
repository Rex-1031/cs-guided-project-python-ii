"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
  # Return "invalid" if n exceeds the length of the list
    if n > len(a):
        return "invalid"
    elif n == 0:
        return []
    else:
        return a[-n:]

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))

# Think of the slicing operator as a function, slice(start,end,stepSize) where only the first arg is required
# The minimalist syntax is [start:end:stepSize]
# and exluding arguments is just like calling the function without arguments
# ex: mylist[2:] is equivalent to slice(2), using the default end value

