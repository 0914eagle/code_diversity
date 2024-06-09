
import random

def solve(expression):
    integers = expression.split('+')
    num_integers = len(integers)
    num_distinct = 1
    for i in range(num_integers - 1):
        if random.randint(0, 1) == 0:
            num_distinct *= len(integers[i])
        else:
            num_distinct *= len(integers[i + 1])
    return num_distinct

