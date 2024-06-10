
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    def custom_sort(s):
        return (len(s), s)

    sorted_lst = sorted(lst, key=custom_sort)
    filtered_lst = [s for s in sorted_lst if len(s) % 2 == 0]
    return filtered_lst

# Test the function with example inputs
print(sorted_list_sum(['aa', 'a', 'aaa']))
print(sorted_list_sum(['ab', 'a', 'aaa', 'cd']))
