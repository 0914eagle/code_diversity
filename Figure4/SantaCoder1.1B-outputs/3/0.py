from typing import List


def below_zero(operations: List[int]) -> bool:
    
    if not operations:
        return True
    if operations[0] > 0:
        return False
    return below_zero(operations[1:]) or operations[0] < 0


if