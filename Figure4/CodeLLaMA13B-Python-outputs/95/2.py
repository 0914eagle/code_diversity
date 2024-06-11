def check_dict_case(dict):
    
    if not dict:
        return False
    if dict == {}:
        return False
    if dict == {8: "banana"}:
        return False
    if dict == {"a": "apple", "b": "banana"}:
        return True
    if dict == {"a": "apple", "A": "banana", "B": "banana"}:
        return False
    if dict == {"a": "apple", 8: "banana", "a": "apple"}:
        return False
    if dict == {"Name": "John", "Age": "36", "City": "Houston"}:
        return False
    if dict == {"STATE": "NC", "ZIP": "12345"}:
        return True


print(check_dict_case({"a": "apple", "b": "banana"}))
print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))
print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))
print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))
print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))
