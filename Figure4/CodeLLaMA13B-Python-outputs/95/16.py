def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        return True if len(set(map(lambda x: x.islower(), dict.keys()))) == 1 or len(set(map(lambda x: x.isupper(), dict.keys()))) == 1 else False


if __name__ == '__main__':
    print(check_dict_case({"a":"apple", "b":"banana"}) )
    print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) )
    print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) )
    print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) )
    print(check_dict_case({"STATE":"NC", "ZIP":"12345" }) )
