from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        else:
            balance -= operation
    return balance < 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
