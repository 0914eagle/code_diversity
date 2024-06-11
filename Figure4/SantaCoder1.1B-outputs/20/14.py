from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest pair")

    # Sort the list of numbers
    numbers.sort()

    # Find the two numbers that are closest to each other
    closest_numbers = []
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < abs(numbers[i] - numbers[i - 1]):
            closest_numbers.append(numbers[i])
        else:
            closest_numbers.append(numbers[i + 1])

    return closest_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
