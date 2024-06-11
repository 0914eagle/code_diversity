from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers")

    min_diff = float("inf")
    first_number = None
    second_number = None

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                first_number = numbers[i]
                second_number = numbers[j]

    return first_number, second_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
