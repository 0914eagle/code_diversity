def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        return True if len(set(map(lambda x: x.islower(), dict.keys()))) == 1 or len(set(map(lambda x: x.isupper(), dict.keys()))) == 1 else False


print(check_dict_case({"a":"apple", "b":"banana"}) )#True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) )#False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) )#False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) )#False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }) )#True
print(check_dict_case({}) )#False