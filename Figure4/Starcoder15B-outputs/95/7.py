def check_dict_case(dict):
    
    if not dict:
        return False
    keys = dict.keys()
    if all(isinstance(key, str) for key in keys):
        if all(key.islower() for key in keys) or all(key.isupper() for key in keys):
            return True
    return False

