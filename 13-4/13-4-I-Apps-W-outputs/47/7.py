
import itertools

def solve(n, k, nums):
    # convert the input string to a list of integers
    nums = [int(num) for num in nums]
    
    # initialize the result
    result = 0
    
    # iterate over all possible combinations of pluses
    for combination in itertools.combinations(range(1, n), k):
        # initialize the current expression
        expression = 0
        
        # iterate over the digits and pluses
        for i in range(n):
            # if the current position is a plus, add the previous digit to the expression
            if i in combination:
                expression += nums[i-1]
            # if the current position is not a plus, add the current digit to the expression
            else:
                expression += nums[i]
        
        # add the result of the current expression to the total result
        result = (result + expression) % (10**9 + 7)
    
    # return the result modulo 10^9 + 7
    return result

