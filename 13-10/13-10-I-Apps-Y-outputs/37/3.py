
def find_smallest_missing_letter(s):
    # Initialize a set to store the unique characters in the string
    unique_chars = set()
    
    # Iterate through the string and add each character to the set
    for char in s:
        unique_chars.add(char)
    
    # Iterate through the lowercase English alphabet and check if each character is in the set
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in unique_chars:
            return char
    
    # If every lowercase English letter occurs in the string, return None
    return None

def main():
    s = input()
    print(find_smallest_missing_letter(s))

if __name__ == '__main__':
    main()

