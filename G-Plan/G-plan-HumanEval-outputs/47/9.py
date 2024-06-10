
def check_if_last_char_is_a_letter(txt: str) -> bool:
    def is_alphabet(char):
        return char.isalpha()

    def is_space(char):
        return char == ' '

    i = len(txt) - 1
    while i >= 0 and is_space(txt[i]):
        i -= 1

    if i < 0:
        return False

    if is_alphabet(txt[i]):
        j = i - 1
        while j >= 0 and not is_space(txt[j]):
            if is_alphabet(txt[j]):
                return False
            j -= 1
        return True

    return False

if __name__ == "__main__":
    txt = input().strip()
    print(check_if_last_char_is_a_letter(txt))
