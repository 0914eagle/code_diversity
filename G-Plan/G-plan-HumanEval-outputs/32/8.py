
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    def custom_sort(s):
        return (len(s), s)

    sorted_lst = sorted(lst, key=custom_sort)
    filtered_lst = [s for s in sorted_lst if len(s) % 2 == 0]
    
    return filtered_lst

# Test cases
input_list = input().strip()[1:-1].split(', ')
result = sorted_list_sum(input_list)
print(result)
