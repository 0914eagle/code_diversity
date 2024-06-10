
def get_substring_length(substring, string):
    
    length = 0
    for i in range(len(substring)):
        if substring[i] != string[i]:
            break
        length += 1
    return length

def get_min_replacements(substring, string):
    
    substring_length = len(substring)
    string_length = len(string)
    if substring_length > string_length:
        return 0
    longest_substring_length = get_substring_length(substring, string)
    return substring_length - longest_substring_length

def main():
    substring = input("Enter the name of the AI: ")
    string = input("Enter the name of the phone: ")
    replacements = get_min_replacements(substring, string)
    print(replacements)

if __name__ == '__main__':
    main()

