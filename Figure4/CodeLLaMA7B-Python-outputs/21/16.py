from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required")
    min_value = min(numbers)
    max_value = max(numbers)
    return [
        (number - min_value) / (max_value - min_value)
        for number in numbers
    ]


if __name__ == "__main__":
    import doctest
    doctest