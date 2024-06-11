from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [delimeter] + [x for pair in zip(numbers, numbers[1:]) for x in pair]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
