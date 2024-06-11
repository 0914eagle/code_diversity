from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [
        number
        for pair in zip(numbers, numbers[1:])
        for number in pair + (delimeter,)
    ]


if __name__ == "__main__":
    import doctest

    do