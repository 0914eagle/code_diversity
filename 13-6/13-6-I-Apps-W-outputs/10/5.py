
def get_unread_letters(letter_states):
    return [i for i, state in enumerate(letter_states) if state == 0]

def get_read_letters(letter_states):
    return [i for i, state in enumerate(letter_states) if state == 1]

def get_next_unread_letter(current_letter, letter_states):
    unread_letters = get_unread_letters(letter_states)
    if current_letter == len(letter_states) - 1:
        return None
    return unread_letters[unread_letters.index(current_letter) + 1]

def get_previous_unread_letter(current_letter, letter_states):
    unread_letters = get_unread_letters(letter_states)
    if current_letter == 0:
        return None
    return unread_letters[unread_letters.index(current_letter) - 1]

def get_minimum_operations(letter_states):
    unread_letters = get_unread_letters(letter_states)
    operations = 0
    current_letter = 0
    while unread_letters:
        next_letter = get_next_unread_letter(current_letter, letter_states)
        if next_letter:
            operations += 1
            current_letter = next_letter
        else:
            previous_letter = get_previous_unread_letter(current_letter, letter_states)
            if previous_letter:
                operations += 1
                current_letter = previous_letter
            else:
                break
    return operations

def main():
    letter_states = list(map(int, input().split()))
    print(get_minimum_operations(letter_states))

if __name__ == '__main__':
    main()

