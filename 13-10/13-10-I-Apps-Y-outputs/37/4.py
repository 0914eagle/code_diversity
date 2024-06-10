
def get_smallest_letter(s):
    # Initialize a set to store the unique letters in the string
    unique_letters = set()
    
    # Loop through each letter in the string
    for letter in s:
        # Check if the letter is already in the set
        if letter not in unique_letters:
            # If not, add it to the set
            unique_letters.add(letter)
    
    # Initialize a list to store the letters in alphabetical order
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Loop through each letter in the alphabet
    for letter in alphabet:
        # Check if the letter is not in the set of unique letters
        if letter not in unique_letters:
            # If it's not, return the letter
            return letter
    
    # If every letter occurs in the string, return None
    return None

def main():
    # Read a string from standard input
    s = input()
    
    # Get the lexicographically smallest letter that does not occur in the string
    smallest_letter = get_smallest_letter(s)
    
    # Print the result
    print(smallest_letter)

if __name__ == '__main__':
    main()

