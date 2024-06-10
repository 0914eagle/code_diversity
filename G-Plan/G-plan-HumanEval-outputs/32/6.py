
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    def custom_sort(s):
        return (len(s), s)

    sorted_lst = sorted(lst, key=custom_sort)
    filtered_lst = [word for word in sorted_lst if len(word) % 2 == 0]

    return filtered_lst

# Read input list of strings
input_lst = input().strip().split()

# Call the function and print the result
print(sorted_list_sum(input_lst))
