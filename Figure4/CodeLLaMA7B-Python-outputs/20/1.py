from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    min_diff = float("inf")
    first_num = None
    second_num = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                first_num = numbers[i]
                second_num = numbers[j]
    return first_num, second_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
