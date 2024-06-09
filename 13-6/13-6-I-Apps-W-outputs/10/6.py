
def get_read_letters(letter_list):
    return sum(letter_list)

def get_unread_letters(letter_list):
    return len(letter_list) - get_read_letters(letter_list)

def get_min_operations(letter_list):
    unread_letters = get_unread_letters(letter_list)
    if unread_letters == 0:
        return 0
    return unread_letters + get_min_operations(letter_list[1:])

def main():
    letter_list = list(map(int, input().split()))
    print(get_min_operations(letter_list))

if __name__ == '__main__':
    main()

