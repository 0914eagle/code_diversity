from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    numbers.sort()
    min_distance = float('inf')
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < min_distance:
            min_distance = numbers[i + 1] - numbers[i]
            closest_numbers = (numbers[i], numbers[i + 1])
    return closest_numbers


if __name__ == '__main__':
    print(find_closest_elements([1.0,