from typing import List


def below_zero(operations: List[int]) -> bool:
    
    for operation in operations:
        if operation < 0:
            return True
    return False


if __name__ == "__main__":
    print(below_zero([1,