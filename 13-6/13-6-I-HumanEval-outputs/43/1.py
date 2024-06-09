
def check_if_last_char_is_a_letter(txt: str) -> bool:
    
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and txt.rfind(last_char) == len(txt) - 1:
        return True
    return False

