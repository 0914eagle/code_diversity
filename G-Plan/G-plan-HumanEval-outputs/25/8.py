
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_diff = float('inf')
    closest_pair = (0, 1)

    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (i - 1, i)

    return numbers[closest_pair[0]], numbers[closest_pair[1]]

if __name__ == "__main__":
    numbers = list(map(float, input().split()))
    result = find_closest_elements(numbers)
    print(result)
