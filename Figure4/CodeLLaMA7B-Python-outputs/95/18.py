def check_dict_case(dict):
    
    # Your code here
    if len(dict) == 0:
        return False
    else:
        for key in dict:
            if type(key) != str:
                return False
            else:
                if key.islower():
                    return True
                elif key.isupper():
                    return True
                else:
                    return False


print(check_dict_case({"a":"apple", "b":"banana"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))
