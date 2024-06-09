
def get_unread_letters(state):
    return [i for i, letter in enumerate(state) if letter == 0]

def get_next_unread_letter(current_letter, state):
    unread_letters = get_unread_letters(state)
    if current_letter == len(state) - 1:
        return unread_letters[0]
    else:
        return unread_letters[unread_letters.index(current_letter) + 1]

def get_previous_unread_letter(current_letter, state):
    unread_letters = get_unread_letters(state)
    if current_letter == 0:
        return unread_letters[-1]
    else:
        return unread_letters[unread_letters.index(current_letter) - 1]

def get_min_operations(state):
    unread_letters = get_unread_letters(state)
    if len(unread_letters) == 0:
        return 0
    min_operations = 0
    current_letter = unread_letters[0]
    while len(unread_letters) > 0:
        min_operations += 1
        current_letter = get_next_unread_letter(current_letter, state)
        unread_letters.remove(current_letter)
    return min_operations

def main():
    n = int(input())
    state = list(map(int, input().split()))
    print(get_min_operations(state))

if __name__ == '__main__':
    main()

