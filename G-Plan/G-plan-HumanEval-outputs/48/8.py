
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    def is_close(num1: float, num2: float, threshold: float) -> bool:
        return abs(num1 - num2) < threshold

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if is_close(numbers[i], numbers[j], threshold):
                return True
    return False

if __name__ == "__main__":
    numbers = list(map(float, input().split()))
    threshold = float(input())
    print(has_close_elements(numbers, threshold))
