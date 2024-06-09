
def check_if_last_char_is_a_letter(txt: str) -> bool:
    

    if not txt:
        return False

    last_char = txt[-1]
    if last_char.isalpha() and txt.split()[-1][-1] == last_char:
        return True
    else:
        return False
