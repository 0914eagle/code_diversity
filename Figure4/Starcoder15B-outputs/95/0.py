def check_dict_case(dict):
    
    # Your code here
    if len(dict) == 0:
        return False
    else:
        for key in dict:
            if type(key) != str:
                return False
            elif key.islower() != dict[key].islower():
                return False
        return True

