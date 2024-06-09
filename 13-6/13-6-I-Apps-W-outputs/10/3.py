
def get_unread_letters(letter_list):
    return [letter for letter in letter_list if letter == 0]

def get_read_letters(letter_list):
    return [letter for letter in letter_list if letter == 1]

def get_min_operations(letter_list):
    unread_letters = get_unread_letters(letter_list)
    read_letters = get_read_letters(letter_list)
    operations = 0
    for letter in unread_letters:
        if letter == 0:
            operations += 1
    for letter in read_letters:
        if letter == 1:
            operations += 1
    return operations

def main():
    letter_list = [int(letter) for letter in input().split()]
    print(get_min_operations(letter_list))

if __name__ == '__main__':
    main()

