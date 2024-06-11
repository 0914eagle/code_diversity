def check_dict_case(dict):
    
    # your code here
    if not dict:
        return False
    else:
        return all(isinstance(k, str) and k.islower() for k in dict.keys()) or all(isinstance(k, str) and k.isupper() for k in dict.keys())


