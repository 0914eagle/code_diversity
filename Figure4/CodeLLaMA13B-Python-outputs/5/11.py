from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [
        delimeter if i % 2 else numbers[i // 2]
        for i in range(2 * len(numbers))
        if i < len(numbers) * 2
    ]


if __name__ == "__