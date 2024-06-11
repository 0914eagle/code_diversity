def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        if all(isinstance(key, str) for key in dict.keys()):
            if all(key.islower() for key in dict.keys()) or all(key.isupper() for key in dict.keys()):
                return True
            else:
                return False
        else:
            return False
