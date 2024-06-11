from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [
        number
        for pair in zip(numbers, numbers[1:] + [numbers[0]])
        for number in pair
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
