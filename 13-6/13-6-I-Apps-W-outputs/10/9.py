
def get_unread_letters(letter_list):
    return [letter for letter in letter_list if letter == 0]

def get_read_letters(letter_list):
    return [letter for letter in letter_list if letter == 1]

def get_min_operations(letter_list):
    unread_letters = get_unread_letters(letter_list)
    read_letters = get_read_letters(letter_list)
    operations = 0
    while unread_letters:
        operations += 1
        current_letter = unread_letters.pop(0)
        if current_letter in read_letters:
            read_letters.remove(current_letter)
    return operations

def main():
    letter_list = list(map(int, input().split()))
    print(get_min_operations(letter_list))

if __name__ == '__main__':
    main()

