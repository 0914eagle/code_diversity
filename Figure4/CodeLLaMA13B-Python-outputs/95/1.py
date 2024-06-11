def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        return all(k.islower() for k in dict) or all(k.isupper() for k in dict)


# Pybites solution
