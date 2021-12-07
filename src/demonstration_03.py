"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""


def multiply_nums(nums):
    code = nums.replace(', ', '*') # turns 2, 3 into 2*3
    return eval(code) # evaluate a string as Python code

print(multiply_nums("1, 2, 3, 4"))



# Alternate solutions:
def alt_multiply_nums(nums):
    # initalize the product
    product = 1

    # Separate the nums string out into a list of numbers
    numberList = nums.split(', ')

    # multiply those numbers together
    for i in numberList:
        product *= int(i)

    return product

