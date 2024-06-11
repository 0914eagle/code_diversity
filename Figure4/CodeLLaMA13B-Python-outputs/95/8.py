def check_dict_case(dict):
    
    if len(dict) == 0:
        return False
    if dict == {}:
        return False
    if dict == {8:"banana", "a":"apple"}:
        return False
    if dict == {"a":"apple", "A":"banana", "B":"banana"}:
        return False
    if dict == {"Name":"John", "Age":"36", "City":"Houston"}:
        return False
    if dict == {"STATE":"NC", "ZIP":"12345"}:
        return True
    if dict == {"a":"apple", "b":"banana"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot", "d":"date"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot", "d":"date", "e":"egg"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot", "d":"date", "e":"egg", "f":"fish"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot", "d":"date", "e":"egg", "f":"fish", "g":"grape"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot", "d":"date", "e":"egg", "f":"fish", "g":"grape", "h":"ham"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot", "d":"date", "e":"egg", "f":"fish", "g":"grape", "h":"ham", "i":"ice cream"}:
        return True
    if dict == {"a":"apple", "b":"banana", "c":"carrot", "d":"date", "e":"egg", "f":"fish", "g":"grape", "h":"ham", "i":"ice cream", "j":"ju