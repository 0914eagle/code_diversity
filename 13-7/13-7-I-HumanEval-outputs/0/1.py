
from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    
    if not dict:
        return False
    lower_case = True
    upper_case = True
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.islower() and upper_case:
            upper_case = False
        elif key.isupper() and lower_case:
            lower_case = False
        else:
            return False
    return True

