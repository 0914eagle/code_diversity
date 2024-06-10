
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    def are_close(num1, num2, threshold):
        return abs(num1 - num2) < threshold

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if are_close(numbers[i], numbers[j], threshold):
                return True
    return False

if __name__ == "__main__":
    input_numbers = list(map(float, input().split()))
    threshold = float(input())
    print(has_close_elements(input_numbers, threshold))
