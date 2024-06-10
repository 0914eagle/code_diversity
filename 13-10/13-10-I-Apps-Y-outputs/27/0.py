
def check_if_two_kinds_of_characters(s):
    # Initialize a dictionary to store the count of each character
    char_count = {}
    
    # Loop through each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1
    
    # Check if there are exactly two kinds of characters
    if len(char_count) == 2:
        # Initialize a variable to store the count of the first character
        first_char_count = 0
        # Loop through each character in the dictionary
        for char, count in char_count.items():
            # If the count is greater than the first character count, set the first character count to the current count
            if count > first_char_count:
                first_char_count = count
            # If the count is less than the first character count, return False
            elif count < first_char_count:
                return False
        # If the first character count is not equal to 2, return False
        if first_char_count != 2:
            return False
        # Otherwise, return True
        return True
    # If there are not exactly two kinds of characters, return False
    else:
        return False

def main():
    s = input("Enter a 4-character string: ")
    if len(s) != 4:
        print("Invalid input")
    else:
        if check_if_two_kinds_of_characters(s):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

