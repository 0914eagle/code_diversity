def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    else:
        return True if len(set([k.islower() for k in dict.keys()])) == 1 else False


#Tests
print check_dict_case({"a":"apple", "b":"banana"})
print check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
print check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
print check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
print check_dict_case({"STATE":"NC", "ZIP":"12345" })


















































































































































































































































































































































