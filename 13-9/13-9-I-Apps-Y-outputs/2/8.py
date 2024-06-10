
def get_next_letter(letter):
    return chr(ord(letter) + 1)

def get_next_letter_in_alphabet(letter):
    if letter == 'z':
        return 'a'
    else:
        return get_next_letter(letter)

if __name__ == '__main__':
    letter = input()
    print(get_next_letter_in_alphabet(letter))

