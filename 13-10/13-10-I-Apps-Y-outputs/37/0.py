
def get_lexicographically_smallest_letter_not_in_string(s):
    # Initialize a set to store the unique characters in the string
    unique_chars = set()
    
    # Iterate through the string and add each character to the set
    for char in s:
        unique_chars.add(char)
    
    # Iterate through the alphabet and check if each character is in the set
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in unique_chars:
            return char
    
    # If every character is in the set, return None
    return None

def main():
    s = input()
    print(get_lexicographically_smallest_letter_not_in_string(s))

if __name__ == '__main__':
    main()

