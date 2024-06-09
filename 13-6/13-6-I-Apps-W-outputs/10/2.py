
def get_unread_letters(letter_list):
    return [letter for letter in letter_list if letter == 0]

def get_read_letters(letter_list):
    return [letter for letter in letter_list if letter == 1]

def get_min_operations(letter_list):
    unread_letters = get_unread_letters(letter_list)
    read_letters = get_read_letters(letter_list)
    min_operations = 0
    while len(unread_letters) > 0:
        if len(read_letters) > 0:
            min_operations += 1
            unread_letters.append(read_letters.pop())
        else:
            min_operations += 1
            unread_letters.pop()
    return min_operations

def main():
    letter_list = list(map(int, input().split()))
    print(get_min_operations(letter_list))

if __name__ == '__main__':
    main()

