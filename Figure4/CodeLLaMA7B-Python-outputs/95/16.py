def check_dict_case(dict):
    
    if not dict:
        return False
    return all(isinstance(k, str) and k.islower() for k in dict.keys()) or all(isinstance(k, str) and k.isupper() for k in dict.keys())


