from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [delimeter if i % 2 == 0 else number for i, number in enumerate(numbers)]


if __name__ == "__main__":
    import doctest

    doctest.test