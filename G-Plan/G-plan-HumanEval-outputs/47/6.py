
def is_alphabet(char):
    return char.isalpha()

def check_if_last_char_is_a_letter(txt: str) -> bool:
    if not txt:
        return False

    i = len(txt) - 1
    while i >= 0 and txt[i] == ' ':
        i -= 1

    if i < 0:
        return False

    if not is_alphabet(txt[i]):
        return False

    while i >= 0 and txt[i] != ' ':
        i -= 1

    return i < 0 or txt[i] == ' '

if __name__ == "__main__":
    txt = input().strip()
    print(check_if_last_char_is_a_letter(txt))
