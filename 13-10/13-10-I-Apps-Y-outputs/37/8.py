
def get_smallest_missing_letter(s):
    # Initialize a set to store the unique characters in the string
    unique_chars = set()
    
    # Iterate through the string and add each character to the set
    for char in s:
        unique_chars.add(char)
    
    # Initialize a variable to store the smallest missing letter
    smallest_missing_letter = ''
    
    # Iterate through the lowercase English alphabet
    for char in 'abcdefghijklmnopqrstuvwxyz':
        # If the current character is not in the set, set it as the smallest missing letter
        if char not in unique_chars:
            smallest_missing_letter = char
            break
    
    # If the smallest missing letter is an empty string, all lowercase English letters occur in the string
    if smallest_missing_letter == '':
        smallest_missing_letter = None
    
    # Return the smallest missing letter
    return smallest_missing_letter

def main():
    s = input()
    smallest_missing_letter = get_smallest_missing_letter(s)
    print(smallest_missing_letter)

if __name__ == '__main__':
    main()

