def check_dict_case(dict):
    
    if not dict:
        return False
    return all(type(k) == str and k.islower() for k in dict) or all(type(k) == str and k.isupper() for k in dict)


