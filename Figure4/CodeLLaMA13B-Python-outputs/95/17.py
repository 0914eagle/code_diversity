def check_dict_case(dict):
    
    if not dict:
        return False
    if dict.keys()[0].isupper():
        for key in dict:
            if not key.isupper():
                return False
    else:
        for key in dict:
            if not key.islower():
                return False
    return True

