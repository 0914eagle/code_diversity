from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    

    if len(numbers) == 0:
        return []

    result = [numbers[0]]

    for number in numbers[1:]:
        result.extend([delimeter, number])

    return result


if __name__ == "__main__":
    import