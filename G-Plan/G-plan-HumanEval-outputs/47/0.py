
def check_if_last_char_is_a_letter(txt: str) -> bool:
    def is_alphabet(char):
        return char.isalpha()

    def is_part_of_word(txt, idx):
        while idx >= 0 and txt[idx] != ' ':
            idx -= 1
        return idx >= 0 and txt[idx] == ' '

    idx = len(txt) - 1
    while idx >= 0 and txt[idx] == ' ':
        idx -= 1

    if idx < 0:
        return False

    if is_alphabet(txt[idx]) and not is_part_of_word(txt, idx):
        return True
    return False

if __name__ == "__main__":
    txt = input().strip()
    print(check_if_last_char_is_a_letter(txt))
