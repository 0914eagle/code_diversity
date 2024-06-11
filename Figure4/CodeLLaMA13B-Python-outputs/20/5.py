from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    numbers.sort()
    min_diff = float("inf")
    min_pair = None
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < min_diff:
            min_diff = numbers[i + 1] - numbers[i]
            min_pair = (numbers[i], numbers[i + 1])
    return min_pair


if __name__ == "__main__":
    import doctest
