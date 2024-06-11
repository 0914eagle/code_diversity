

def check_dict_case(dict):
    
    if not dict:
        return False

    are_all_lower = all(key.islower() for key in dict.keys())
    are_all_upper = all(key.isupper() for key in dict.keys())

    return are_all_lower or are_all_upper


