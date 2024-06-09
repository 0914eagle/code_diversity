
import itertools

def solve(n, k, digits):
    # calculate the number of ways to place k pluses in the string
    num_ways = itertools.combinations(range(1, n), k)
    
    # initialize the sum
    sum = 0
    
    # iterate over all possible ways to place k pluses
    for way in num_ways:
        # calculate the result of the arithmetic expression
        result = 0
        for i in range(n - 1):
            if i + 1 in way:
                result += int(digits[i])
            else:
                result *= int(digits[i])
        # add the result to the sum
        sum += result
    
    # return the sum modulo 10^9 + 7
    return sum % 1000000007

