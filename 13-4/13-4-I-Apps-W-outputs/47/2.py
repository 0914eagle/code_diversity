
import itertools

def solve(n, k, digits):
    # convert the string of digits to a list of integers
    digits = [int(digit) for digit in digits]
    
    # initialize the result to 0
    result = 0
    
    # iterate over all possible ways to place k pluses in the string
    for pluses in itertools.combinations(range(1, n), k):
        # initialize the current expression to the first digit
        expression = digits[0]
        
        # iterate over the remaining digits and pluses
        for i, plus in enumerate(pluses):
            # add the current digit to the expression
            expression += digits[plus + i]
            
        # add the result of the expression to the total
        result += expression
    
    # return the result modulo 10^9 + 7
    return result % 1000000007

