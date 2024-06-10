
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

# Read input list
input_list = input().strip().split(',')
input_list = [eval(item.strip()) for item in input_list]

# Call the function and print the result
result = filter_integers(input_list)
print(result)
