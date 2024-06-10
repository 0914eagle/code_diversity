
def smallest_missing_letter(s):
    # Initialize a set to store the unique characters in the string
    char_set = set()
    
    # Iterate through the string and add each character to the set
    for char in s:
        char_set.add(char)
    
    # Iterate through the alphabet and check if each character is in the set
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in char_set:
            return char
    
    # If every character is in the set, return None
    return None

def main():
    s = input()
    print(smallest_missing_letter(s))

if __name__ == '__main__':
    main()

