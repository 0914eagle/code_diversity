def check_dict_case(dict):
    
    if not dict:
        return False
    if dict.keys()[0].isupper():
        for key in dict.keys():
            if not key.isupper():
                return False
    else:
        for key in dict.keys():
            if not key.islower():
                return False
    return True


if __name__ == "__main__":
    print check_dict_case({"a":"apple", "b":"banana"})
    print check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
    print check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
    print check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
    print check_dict_case({"STATE":"NC", "ZIP":"12345" })
