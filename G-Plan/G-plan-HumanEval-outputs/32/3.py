
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    def custom_sort(s):
        return (len(s), s)

    sorted_list = sorted(lst, key=custom_sort)
    filtered_list = [s for s in sorted_list if len(s) % 2 == 0]
    return filtered_list

# Test the function with example inputs
print(sorted_list_sum(['aa', 'a', 'aaa']))
print(sorted_list_sum(['ab', 'a', 'aaa', 'cd']))
