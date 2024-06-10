
from typing import List

def make_a_pile(n: int) -> List[int]:
    
    # Initialize the list to store the number of stones in each level
    levels = [n]

    # Iterate from the second level to the last level
    for i in range(n-1):
        # If the number of stones in the previous level is odd,
        # the number of stones in the current level is the next odd number
        if levels[i] % 2 == 1:
            levels.append(levels[i] + 1)
        # If the number of stones in the previous level is even,
        # the number of stones in the current level is the next even number
        else:
            levels.append(levels[i] + 2)

    return levels

