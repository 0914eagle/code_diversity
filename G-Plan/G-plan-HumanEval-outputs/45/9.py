
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
input_list = input().strip().split()
numbers = [int(num) for num in input_list]
result = remove_duplicates(numbers)
print(result)
