from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [delimeter if i % 2 == 1 else x for i, x in enumerate(numbers)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
