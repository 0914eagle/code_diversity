from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [delimeter] * (len(numbers) * 2 - 1) or numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
