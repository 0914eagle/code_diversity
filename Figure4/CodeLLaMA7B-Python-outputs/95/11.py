def check_dict_case(dict):
    
    # check if dict is empty
    if len(dict) == 0:
        return False
    # check if all keys are strings
    if not all(isinstance(key, str) for key in dict.keys()):
        return False
    # check if all keys are lower case or upper case
    return all(key.islower() or key.isupper() for key in dict.keys())


