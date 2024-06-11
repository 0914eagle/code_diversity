def check_dict_case(dict):
    
    # check if dict is empty
    if len(dict) == 0:
        return False
    # check if all keys are lower case
    for key in dict:
        if not isinstance(key, str):
            return False
        if key.islower() == False:
            return False
    return True


print(check_dict_case({"a":"apple", "b":"banana"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))