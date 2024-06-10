
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_set = set()
    result = []
    
    for num in numbers:
        if num not in unique_set:
            result.append(num)
            unique_set.add(num)
    
    return result

# Test the function with the provided example
input_list = input().strip().split()
input_list = [int(num) for num in input_list]
print(remove_duplicates(input_list))
