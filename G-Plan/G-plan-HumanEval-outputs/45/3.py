
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_elements = set()
    result = []
    
    for num in numbers:
        if num not in unique_elements:
            result.append(num)
            unique_elements.add(num)
    
    return result

# Read input
input_numbers = input().strip().split()
numbers = [int(num) for num in input_numbers]

# Call the function and print the result
print(remove_duplicates(numbers))
