def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    if len(dict) == 1:
        return True
    if len(dict) > 1:
        if dict[list(dict.keys())[0]].isupper() == True:
            for i in dict:
                if dict[i].isupper() == False:
                    return False
            return True
        elif dict[list(dict.keys())[0]].islower() == True:
            for i in dict:
                if dict[i].islower() == False:
                    return False
            return True
        else:
            return False


#