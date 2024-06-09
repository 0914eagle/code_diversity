
from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    
    if not dict:
        return False
    
    is_lower = False
    is_upper = False
    
    for key in dict:
        if key.islower():
            is_lower = True
        elif key.isupper():
            is_upper = True
        else:
            return False
    
    return is_lower or is_upper

