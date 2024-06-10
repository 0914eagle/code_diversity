
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_elements = set()
    result = []
    
    for num in numbers:
        if num not in unique_elements:
            result.append(num)
            unique_elements.add(num)
    
    return result

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    result = remove_duplicates(numbers)
    print(result)
