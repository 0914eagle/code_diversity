
def get_meow_factor(string):
    # Initialize variables
    meow_factor = 0
    string_length = len(string)
    word = "meow"
    word_length = len(word)
    
    # Loop through each substring of the string
    for i in range(string_length - word_length + 1):
        # Check if the substring matches the word "meow"
        if string[i:i+word_length] == word:
            # If it matches, return the meow factor
            return meow_factor
        # If it doesn't match, increment the meow factor and try the next substring
        meow_factor += 1
    
    # If the word "meow" is not found in the string, return -1
    return -1

def main():
    string = input("Enter a string: ")
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

