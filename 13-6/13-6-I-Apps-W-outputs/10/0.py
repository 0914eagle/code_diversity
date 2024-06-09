
def get_unread_letters(letter_list):
    return [letter for letter in letter_list if letter == 0]

def get_read_letters(letter_list):
    return [letter for letter in letter_list if letter == 1]

def get_next_unread_letter(current_letter, unread_letters):
    current_index = unread_letters.index(current_letter)
    if current_index == len(unread_letters) - 1:
        return None
    return unread_letters[current_index + 1]

def get_previous_unread_letter(current_letter, unread_letters):
    current_index = unread_letters.index(current_letter)
    if current_index == 0:
        return None
    return unread_letters[current_index - 1]

def get_minimum_operations(letter_list):
    unread_letters = get_unread_letters(letter_list)
    read_letters = get_read_letters(letter_list)
    current_letter = unread_letters[0]
    operations = 0
    while len(unread_letters) > 0:
        next_unread_letter = get_next_unread_letter(current_letter, unread_letters)
        if next_unread_letter:
            operations += 1
            current_letter = next_unread_letter
        else:
            previous_unread_letter = get_previous_unread_letter(current_letter, unread_letters)
            if previous_unread_letter:
                operations += 1
                current_letter = previous_unread_letter
            else:
                break
    return operations + len(read_letters)

if __name__ == '__main__':
    letter_list = [int(letter) for letter in input().split()]
    print(get_minimum_operations(letter_list))

