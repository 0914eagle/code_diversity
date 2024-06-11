def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        dict_keys = list(dict.keys())
        if all(isinstance(x, str) for x in dict_keys):
            if all(x.islower() for x in dict_keys) or all(x.isupper() for x in dict_keys):
                return True
            else:
                return False
        else:
            return False

