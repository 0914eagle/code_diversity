
def get_next_string(s):
    # Initialize an empty string to store the next string
    next_string = ""
    
    # Iterate through the characters of the input string
    for char in s:
        # If the current character is a digit, append it to the next string
        if char.isdigit():
            next_string += char
        # If the current character is not a digit, append the next character to the next string
        else:
            next_string += str(int(char) + 1)
    
    # Return the next string
    return next_string

def get_kth_char(s, k):
    # Initialize a counter to keep track of the length of the string
    length = 0
    
    # Iterate through the characters of the input string
    for char in s:
        # If the current character is a digit, increment the length by 1
        if char.isdigit():
            length += 1
        # If the current character is not a digit, increment the length by the number of times the digit appears in the string
        else:
            length += int(char)
        
        # If the length is greater than or equal to the input k, return the current character
        if length >= k:
            return char
    
    # If the length is less than the input k, return None
    return None

def main():
    s = input("Enter the string: ")
    k = int(input("Enter the position: "))
    
    # Initialize a variable to store the string after 5*10^15 days
    after_days = ""
    
    # Iterate 5*10^15 times to get the string after 5*10^15 days
    for _ in range(50000000000000000):
        after_days = get_next_string(after_days)
    
    # Get the K-th character from the left in the string after 5*10^15 days
    char = get_kth_char(after_days, k)
    
    # Print the result
    print(char)

if __name__ == '__main__':
    main()

