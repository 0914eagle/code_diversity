from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to find the closest")
    closest_numbers = []
    for number in numbers:
        closest_numbers.append(abs(number - numbers[0]))
    closest_numbers.sort()
    return numbers[closest_numbers.index(closest_numbers[0])], numbers[closest_numbers.index(closest_numbers[1])]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
