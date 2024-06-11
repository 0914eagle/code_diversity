from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    min_number = min(numbers)
    max_number = max(numbers)
    return [
        (number - min_number) / (max_number - min_number)
        for number in numbers
    ]


if __name__ == "__main__":
    import doctest
   