def check_dict_case(dict):
    
    if not dict:
        return False
    for key in dict:
        if not isinstance(key, str):
            return False
        if not key.islower():
            return False
        if not key.isupper():
            return False
    return True


