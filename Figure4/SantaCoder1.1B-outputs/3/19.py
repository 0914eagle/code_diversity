from typing import List


def below_zero(operations: List[int]) -> bool:
    
    if len(operations) == 0:
        return False
    elif len(operations) == 1:
        return operations[0] < 0
    else:
        return operations[0] < 0 and operations[-1] > 0


if