"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    return sum(l in "aeiouAEIOU" for l in input_str)


# more verbose alt solution:
def alt_get_count(input_str):
    # Your code here
    count = 0
    for l in input_str:
        if l in "aeiouAEIOU":
            count += 1
    return count

