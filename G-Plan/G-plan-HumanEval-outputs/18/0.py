
from typing import List
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    window = deque()
    
    for i, num in enumerate(numbers):
        while window and numbers[window[-1]] <= num:
            window.pop()
        window.append(i)
        
        if window[0] == i - len(window):
            window.popleft()
        
        result.append(numbers[window[0]])
    
    return result

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    result = rolling_max(numbers)
    print(result)
