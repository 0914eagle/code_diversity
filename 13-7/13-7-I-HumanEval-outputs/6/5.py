
def check_if_last_char_is_a_letter(txt: str) -> bool:
    
    if not txt:
        return False
    if txt[-1].isalpha() and txt[-1] not in 'aeiou':
        return True
    return False

