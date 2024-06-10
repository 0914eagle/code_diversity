
def check_if_last_char_is_a_letter(txt: str) -> bool:
    def is_alphabet(char):
        return char.isalpha()

    def is_part_of_word(txt, index):
        if index == len(txt) - 1 or txt[index + 1] == ' ':
            return False
        return True

    i = len(txt) - 1
    while i >= 0:
        if txt[i] == ' ':
            i -= 1
        else:
            if is_alphabet(txt[i]) and not is_part_of_word(txt, i):
                return True
            else:
                return False
    return False

if __name__ == "__main__":
    txt = input().strip()
    print(check_if_last_char_is_a_letter(txt))
