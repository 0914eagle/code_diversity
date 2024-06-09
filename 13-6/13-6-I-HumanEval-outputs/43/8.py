
def check_if_last_char_is_a_letter(txt: str) -> bool:
    

    if not txt:
        return False

    last_char = txt[-1]
    if last_char.isalpha():
        if txt.endswith(' '):
            return False
        else:
            return True
    else:
        return False

