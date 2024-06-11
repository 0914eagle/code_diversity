from typing import List


def below_zero(operations: List[int]) -> bool:
    
    if not operations:
        return False
    if operations[0] < 0:
        return True
    return False


if __name__ == '__main__':
    import doctest
   