
import itertools

def solve(n, k, digits):
    # calculate the number of ways to place k pluses in the string
    num_ways = itertools.combinations(range(1, n), k)
    
    # initialize the sum
    sum = 0
    
    # iterate over all possible ways to place k pluses
    for way in num_ways:
        # calculate the value of the arithmetic expression
        value = 0
        for i in range(n - 1):
            if i + 1 in way:
                value += int(digits[i])
            else:
                value += int(digits[i]) * int(digits[i + 1])
        
        # add the value to the sum
        sum += value
    
    # return the sum modulo 10^9 + 7
    return sum % 1000000007

