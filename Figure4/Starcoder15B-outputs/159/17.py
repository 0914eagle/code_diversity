def eat(number, need, remaining):
    
    # your code here
    return [number + need, remaining - need]

# Test
print(eat(5, 6, 10))
print(eat(4, 8, 9))
print(eat(1, 10, 10))
print(eat(2, 11, 5))
/README.md
# Codewars

This repository contains my solutions to the katas on [codewars](https://www.codewars.com).

## Languages

* Python
* JavaScript
/python/8kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is 