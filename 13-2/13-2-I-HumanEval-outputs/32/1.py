
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # delete the strings that have odd lengths from the list
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # sort the list by length of each word
    lst.sort(key=len)
    
    # if two words have the same length, sort them alphabetically
    lst.sort()
    
    return lst

