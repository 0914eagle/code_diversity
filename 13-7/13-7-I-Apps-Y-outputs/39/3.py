
def is_even(s):
    # Check if the string is even
    return s == s[::-1]

def longest_even_substring(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    is_even_substring = False

    # Iterate over the string
    for i in range(len(s)):
        # Check if the current substring is even
        if is_even(s[i:]):
            # If it is even, increment the current length
            current_length += 1
            # Check if the current length is greater than the maximum length
            if current_length > max_length:
                # If it is, update the maximum length
                max_length = current_length
        else:
            # If the current substring is not even, reset the current length
            current_length = 0
    
    # Return the maximum length
    return max_length

def main():
    s = input()
    print(longest_even_substring(s))

if __name__ == '__main__':
    main()

