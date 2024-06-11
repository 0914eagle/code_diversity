def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        for key in dict:
            if type(key) != str:
                return False
            elif key.islower():
                continue
            elif key.isupper():
                continue
            else:
                return False
        return True


