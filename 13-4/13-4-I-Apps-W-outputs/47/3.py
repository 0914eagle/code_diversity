
import itertools

def solve(n, k, line):
    # calculate the number of ways to place k pluses in the line
    num_ways = itertools.combinations(range(1, n), k)
    
    # initialize the sum
    sum = 0
    
    # iterate over the ways to place k pluses
    for way in num_ways:
        # calculate the result of the arithmetic expression
        result = 0
        for i in range(n - 1):
            # if the current position is a plus, add the digits on either side
            if i in way:
                result += int(line[i - 1]) + int(line[i + 1])
            # otherwise, add the digit at the current position
            else:
                result += int(line[i])
        
        # add the result to the sum
        sum += result
    
    # return the sum modulo 10^9 + 7
    return sum % 1000000007

