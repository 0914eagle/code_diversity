
from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    
    if not dict:
        return False
    lowercase_keys = all(key.islower() for key in dict.keys())
    uppercase_keys = all(key.isupper() for key in dict.keys())
    return lowercase_keys or uppercase_keys

