
def is_even_string(s):
    # Check if the string is even
    if len(s) % 2 == 0:
        # Check if the first half is the same as the second half
        return s[:len(s)//2] == s[len(s)//2:]
    else:
        # If the length is odd, the string is not even
        return False

def longest_even_string(s):
    # Initialize the length of the longest even string as 0
    longest_even_len = 0
    # Iterate through the string from the end
    for i in range(len(s)-1, -1, -1):
        # Check if the substring from the beginning to the current index is even
        if is_even_string(s[:i+1]):
            # If it is even, update the longest even length
            longest_even_len = max(longest_even_len, i+1)
    # Return the longest even length
    return longest_even_len

if __name__ == '__main__':
    s = input()
    print(longest_even_string(s))

