
def get_unread_letters(letter_list):
    return [letter for letter in letter_list if letter == 0]

def get_read_letters(letter_list):
    return [letter for letter in letter_list if letter == 1]

def get_minimum_operations(letter_list):
    unread_letters = get_unread_letters(letter_list)
    read_letters = get_read_letters(letter_list)
    operations = 0
    for i in range(len(unread_letters)):
        if i < len(unread_letters) - 1:
            operations += 1
        if i > 0:
            operations += 1
    return operations + len(read_letters)

def main():
    letter_list = list(map(int, input().split()))
    print(get_minimum_operations(letter_list))

if __name__ == '__main__':
    main()

