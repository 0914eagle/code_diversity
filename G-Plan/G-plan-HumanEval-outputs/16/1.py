
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
operations1 = [1, 2, 3]
operations2 = [1, 2, -4, 5]

print(below_zero(operations1))
print(below_zero(operations2))
