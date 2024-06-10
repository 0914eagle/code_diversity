
from typing import List
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    
    result = []
    window = deque()
    
    for i, num in enumerate(numbers):
        while window and numbers[window[-1]] < num:
            window.pop()
        window.append(i)
        
        if i >= len(numbers) - 1:
            result.append(numbers[window[0]])
        elif i - window[0] >= 3:
            window.popleft()
            result.append(numbers[window[0]])
        else:
            result.append(numbers[window[0]])
    
    return result

if __name__ == "__main__":
    numbers = list(map(int, input().strip().split()))
    result = rolling_max(numbers)
    print(*result)
