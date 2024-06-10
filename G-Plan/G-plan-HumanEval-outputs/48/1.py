
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    def is_close(a: float, b: float, threshold: float) -> bool:
        return abs(a - b) < threshold

    def has_close_pair(numbers: List[float], threshold: float) -> bool:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if is_close(numbers[i], numbers[j], threshold):
                    return True
        return False

    return has_close_pair(numbers, threshold)

if __name__ == "__main__":
    numbers = list(map(float, input().split()))
    threshold = float(input())
    print(has_close_elements(numbers, threshold))
