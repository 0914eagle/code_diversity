def check_dict_case(dict):
    
    if not dict:
        return False
    else:
        return all(isinstance(key, str) for key in dict.keys()) and all(key.islower() or key.isupper() for key in dict.keys())


print(check_dict_case({"a":"apple", "b":"banana"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))
print(check_dict_case({}))
