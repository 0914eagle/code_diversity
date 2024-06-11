def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        for key in dict:
            if type(key) != str:
                return False
            elif key.islower() == False and key.isupper() == False:
                return False
        return True

