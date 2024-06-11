def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        return True if dict.keys()[0].islower() else False if dict.keys()[0].isupper() else False


if __name__ == '__main__':
    print check_dict_case({"a":"apple", "b":"banana"})
    print check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
    print check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
    print check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
    print check_dict_case({"STATE":"NC", "ZIP":"12345" })
