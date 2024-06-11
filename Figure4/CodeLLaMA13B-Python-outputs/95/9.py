def check_dict_case(dict):
    
    if not dict:
        return False
    return all(k.islower() for k in dict) or all(k.isupper() for k in dict)


if __name__ == '__main__':
    print(check_dict_case({"a":"apple", "b":"banana"}) )
    print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) )
    print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) )
    print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) )
    print(check_dict_case({"STATE":"NC", "ZIP":"12345" }) )
