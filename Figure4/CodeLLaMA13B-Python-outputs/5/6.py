from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    

    if len(numbers) == 0:
        return []
    return [numbers[0]] + intersperse(
        [delimeter] + numbers[1:], delimeter
    ) if len(numbers) > 1 else numbers


if __name__ == "__main__":
    import do