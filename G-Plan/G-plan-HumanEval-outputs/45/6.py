
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_elements = set()
    result = []
    
    for num in numbers:
        if num not in unique_elements:
            result.append(num)
            unique_elements.add(num)
    
    return result

# Test the function with the provided example
input_list = input().strip()
numbers = list(map(int, input_list[1:-1].split(', ')))
print(remove_duplicates(numbers))
