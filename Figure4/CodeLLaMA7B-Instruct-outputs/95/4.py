

def check_dict_case(dict):
    
    if not dict:
        return False

    are_all_lower_case = all(key.islower() for key in dict.keys())
    are_all_upper_case = all(key.isupper() for key in dict.keys())

    return are_all_lower_case or are_all_upper_case


