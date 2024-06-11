def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    for key in dict:
        if not isinstance(key, str):
            return False
        if not key.islower() and not key.isupper():
            return False
    return True

