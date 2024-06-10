
def get_substring_length(substring, main_string):
    return len(substring)

def replace_characters(substring, main_string):
    substring_length = get_substring_length(substring, main_string)
    for i in range(len(main_string) - substring_length + 1):
        if main_string[i:i+substring_length] == substring:
            return i
    return -1

def get_minimum_replacements(substring, main_string):
    replacements = 0
    while True:
        index = replace_characters(substring, main_string)
        if index == -1:
            break
        main_string = main_string[:index] + '#' + main_string[index+1:]
        replacements += 1
    return replacements

def main():
    substring = input("Enter the name of the phone: ")
    main_string = input("Enter the name of the AI: ")
    print(get_minimum_replacements(substring, main_string))

if __name__ == '__main__':
    main()

