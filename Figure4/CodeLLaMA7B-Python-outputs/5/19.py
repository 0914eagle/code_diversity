from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [
        number
        for i, number in enumerate(numbers)
        for _ in range(i % 2 + 1)
    ] + [delimeter]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
