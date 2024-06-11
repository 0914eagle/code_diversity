from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [
        number
        for index, number in enumerate(numbers)
        if index % 2 == 0
        or index == len(numbers) - 1
        and index % 2 == 1
    ]


if __name__ == "__main__":
    import doctest

