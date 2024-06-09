
from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    
    if not dict:
        return False
    keys = dict.keys()
    lower_case_keys = [key for key in keys if key.islower()]
    upper_case_keys = [key for key in keys if key.isupper()]
    if len(lower_case_keys) == len(keys):
        return True
    elif len(upper_case_keys) == len(keys):
        return True
    else:
        return False

