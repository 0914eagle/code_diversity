def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    if len(dict) == 1:
        return True
    if dict[list(dict.keys())[0]].isupper() and dict[list(dict.keys())[1]].isupper():
        return True
    if dict[list(dict.keys())[0]].islower() and dict[list(dict.keys())[1]].islower():
        return True
    return False


# Code of the function
