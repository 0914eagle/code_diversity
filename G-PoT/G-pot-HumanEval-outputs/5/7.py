
def check_if_last_char_is_a_letter(txt: str) -> bool:
    if not txt:
        return False
    last_char = txt.strip()[-1]
    if last_char.isalpha() and (len(txt.split()) == 1 or txt.strip()[-2] == ' '):
        return True
    return False
