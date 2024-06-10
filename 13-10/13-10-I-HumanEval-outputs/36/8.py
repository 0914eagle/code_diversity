
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    even_digits = [2, 4, 6, 8, 0]
    unique_list = []
    for num in x:
        if all(str(num)[i] not in even_digits for i in range(len(str(num)))):
            unique_list.append(num)
    return sorted(unique_list)

