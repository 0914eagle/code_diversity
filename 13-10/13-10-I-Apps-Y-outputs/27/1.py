
def is_double_character(s):
    # Initialize a set to store the unique characters in the string
    unique_chars = set()
    
    # Iterate through the string and check if each character is already in the set
    for char in s:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    
    # If the set only has two characters, return True
    return len(unique_chars) == 2

def main():
    s = input("Enter a 4-character string: ")
    if is_double_character(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

