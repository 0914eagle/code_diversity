from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [
        x for t in zip(numbers[::2], numbers[1::2]) for x in t + (numbers[-1:],)
    ] if numbers else []


if __name__ == "__main__":
    import doctest

    doctest