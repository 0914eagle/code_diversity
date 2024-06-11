def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        if all(isinstance(k, str) for k in dict.keys()):
            if all(k.islower() for k in dict.keys()) or all(k.isupper() for k in dict.keys()):
                return True
            else:
                return False
        else:
            return False

# 2.
