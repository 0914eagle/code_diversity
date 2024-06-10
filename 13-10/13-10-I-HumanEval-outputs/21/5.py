
from typing import List

def f(n: int) -> List[int]:
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate from 1 to n
    for i in range(1, n+1):
        # If i is even, compute the factorial of i and add it to the list
        if i % 2 == 0:
            result.append(math.factorial(i))
        # Otherwise, compute the sum of numbers from 1 to i and add it to the list
        else:
            result.append(sum(range(1, i+1)))
            
    return result

