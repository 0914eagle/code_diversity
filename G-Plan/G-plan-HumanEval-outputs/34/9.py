
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

# Read input values as a list of any Python values
input_values = input().strip().split(',')
values = [eval(val.strip()) for val in input_values]

# Call the filter_integers function and print the result
result = filter_integers(values)
print(result)
