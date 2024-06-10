
def get_kth_character(s, k):
    # Initialize a dictionary to map each digit to its repeated form
    digit_map = {str(i): str(i) * (i + 1) for i in range(1, 10)}
    
    # Initialize an empty string to store the resulting string
    result = ""
    
    # Loop through each character in the input string
    for char in s:
        # If the character is a digit, replace it with its repeated form
        if char in digit_map:
            result += digit_map[char]
        # If the character is not a digit, add it to the result as is
        else:
            result += char
    
    # Return the k-th character from the left in the resulting string
    return result[k - 1]

def main():
    # Read the input string and the value of K from stdin
    s = input()
    k = int(input())
    
    # Call the get_kth_character function and print the result
    print(get_kth_character(s, k))

if __name__ == '__main__':
    main()

