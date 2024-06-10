
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    # Initialize the list to store the number of stones in each level
    levels = [n]

    # Iterate through the levels and calculate the number of stones in each level
    for i in range(n-1):
        # If the current level is odd, the next level will have an odd number of stones
        if levels[i] % 2 == 1:
            levels.append(levels[i] + 1)
        # If the current level is even, the next level will have an even number of stones
        else:
            levels.append(levels[i] + 2)

    return levels

