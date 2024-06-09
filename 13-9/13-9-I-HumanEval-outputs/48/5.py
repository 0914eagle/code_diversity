
from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    
    # Check if the dictionary is empty
    if not dict:
        return False
    
    # Check if all keys are in lower case
    if all(key.islower() for key in dict.keys()):
        return True
    
    # Check if all keys are in upper case
    if all(key.isupper() for key in dict.keys()):
        return True
    
    # If the dictionary has keys that are not in lower or upper case, return False
    return False

