
def get_unread_letters(letter_states):
    return [i for i, state in enumerate(letter_states) if state == 0]

def get_read_letters(letter_states):
    return [i for i, state in enumerate(letter_states) if state == 1]

def get_next_unread_letter(current_letter, letter_states):
    unread_letters = get_unread_letters(letter_states)
    if current_letter in unread_letters:
        return unread_letters[unread_letters.index(current_letter) + 1]
    else:
        return None

def get_previous_unread_letter(current_letter, letter_states):
    unread_letters = get_unread_letters(letter_states)
    if current_letter in unread_letters:
        return unread_letters[unread_letters.index(current_letter) - 1]
    else:
        return None

def get_min_operations(letter_states):
    unread_letters = get_unread_letters(letter_states)
    if len(unread_letters) == 0:
        return 0
    else:
        current_letter = unread_letters[0]
        operations = 1
        while len(get_unread_letters(letter_states)) > 0:
            next_letter = get_next_unread_letter(current_letter, letter_states)
            if next_letter is not None:
                current_letter = next_letter
                operations += 1
            else:
                previous_letter = get_previous_unread_letter(current_letter, letter_states)
                if previous_letter is not None:
                    current_letter = previous_letter
                    operations += 1
                else:
                    break
        return operations

if __name__ == '__main__':
    letter_states = list(map(int, input().split()))
    print(get_min_operations(letter_states))

