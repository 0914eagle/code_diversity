
from typing import List

def odd_count(lst: List[str]) -> List[str]:
    
    return ['the number of odd elements ' + str(len([x for x in lst[i] if int(x) % 2 == 1])) + 'n the str' + str(len(lst[i])) + 'ng ' + str(len(lst[i])) + ' of the ' + str(len(lst[i])) + 'nput.' for i in range(len(lst))]

