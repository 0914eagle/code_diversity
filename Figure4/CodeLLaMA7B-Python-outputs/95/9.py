def check_dict_case(dict):
    
    if not dict:
        return False
    else:
        return all(isinstance(key, str) for key in dict.keys()) and all(key.islower() or key.isupper() for key in dict.keys())


