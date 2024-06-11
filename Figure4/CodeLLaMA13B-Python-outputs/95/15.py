def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        return True if len(set([x.islower() for x in dict.keys()])) == 1 else False


# 2nd solution
