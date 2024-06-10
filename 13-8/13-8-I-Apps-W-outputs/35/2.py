
def find_substring(ai_name, phone_name):
    # Initialize a variable to keep track of the minimum number of characters to replace
    min_replacements = len(ai_name)
    # Loop through each possible starting index of the phone name in the AI name
    for i in range(len(ai_name) - len(phone_name) + 1):
        # Check if the substring starting at index i is equal to the phone name
        if ai_name[i:i+len(phone_name)] == phone_name:
            # If it is, calculate the number of characters that need to be replaced to remove the substring
            replacements = len(phone_name)
            # If the number of replacements is less than the current minimum, update the minimum
            if replacements < min_replacements:
                min_replacements = replacements
    # Return the minimum number of characters to replace
    return min_replacements

def main():
    # Read the input from stdin
    ai_name = input()
    phone_name = input()
    # Call the find_substring function and print the result
    print(find_substring(ai_name, phone_name))

if __name__ == '__main__':
    main()

