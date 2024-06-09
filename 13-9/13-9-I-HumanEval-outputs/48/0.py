
from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    
    # Check if the dictionary is empty
    if not dict:
        return False
    
    # Get the case of the first key
    key_case = "lower" if dict[list(dict.keys())[0]].islower() else "upper"
    
    # Check if all keys have the same case as the first key
    for key in dict:
        if key_case == "lower" and not key.islower():
            return False
        elif key_case == "upper" and not key.isupper():
            return False
    
    # If all keys have the same case as the first key, return True
    return True

