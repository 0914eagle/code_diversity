
from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    
    if not dict:
        return False
    keys = list(dict.keys())
    if len(set(keys)) != len(keys):
        return False
    lower_case = all(key.islower() for key in keys)
    upper_case = all(key.isupper() for key in keys)
    return lower_case or upper_case

