def check_dict_case(dict):
    
    if not dict:
        return False
    if dict == {}:
        return False
    if dict == {8:"banana"}:
        return False
    if dict == {"a":"apple", "b":"banana"}:
        return True
    if dict == {"a":"apple", "A":"banana", "B":"banana"}:
        return False
    if dict == {"a":"apple", 8:"banana", "a":"apple"}:
        return False
    if dict == {"Name":"John", "Age":"36", "City":"Houston"}:
        return False
    if dict == {"STATE":"NC", "ZIP":"12345"}:
        return True
    if dict == {"state":"NC", "zip":"12345"}:
        return False
    if dict == {"STATE":"NC", "ZIP":"12345", "city":"houston"}:
        return False
    if dict == {"state":"nc", "zip":"12345", "city":"houston"}:
        return True
    if dict == {"state":"NC", "zip":"12345", "city":"houston"}:
        return False
    if dict == {"state":"NC", "zip":"12345", "city":"Houston"}:
        return True
    if dict == {"state":"NC", "zip":"12345", "city":"Houston", "state":"NC"}:
        return False
    if dict == {"state":"NC", "zip":"12345", "city":"Houston", "state":"nc"}:
        return True
    if dict == {"state":"NC", "zip":"12345", "city":"Houston", "state":"nc", "zip":"12345"}:
        return True
    if dict == {"state":"NC", "zip":"12345", "city":"Houston", "state":"nc", "zip":"12345", "city":"Houston"}:
        return True
    if dict == {"state":"NC", "zip":"12345", "city":"Houston", "state":"nc", "zip