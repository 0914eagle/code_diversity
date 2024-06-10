
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    def custom_sort(s):
        return (len(s), s)

    sorted_lst = sorted(lst, key=custom_sort)
    filtered_lst = [word for word in sorted_lst if len(word) % 2 == 0]
    
    return filtered_lst

# Read input
input_list = input().strip().split()
result = sorted_list_sum(input_list)

# Print output
print(result)
