def check_dict_case(dict):
    
    if not dict:
        return False
    if all(isinstance(key, str) for key in dict.keys()):
        if all(key.islower() for key in dict.keys()):
            return True
        elif all(key.isupper() for key in dict.keys()):
            return True
        else:
            return False
    else:
        return False

