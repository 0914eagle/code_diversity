from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    

    return [
        x
        for tup in zip(numbers[::2], numbers[1::2])
        for x in tup + (numbers[-1],)
        if x is not None
    ]


if __name__ ==