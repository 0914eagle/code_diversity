
def check_if_last_char_is_a_letter(txt: str) -> bool:
    if not txt:
        return False
    
    txt = txt.strip()
    if txt[-1].isalpha() and (len(txt) == 1 or txt[-2] == ' '):
        return True
    return False
