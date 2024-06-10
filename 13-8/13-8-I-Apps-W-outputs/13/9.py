
def cut_string(s):
    # Initialize variables
    k = 0
    good_strings = []
    
    # Iterate through the string
    for i in range(len(s)):
        # Check if the current substring is good
        if is_good_substring(s[i:]):
            # If it is, add it to the list of good strings
            good_strings.append(s[i:])
            # Increment the number of good strings
            k += 1
    
    # Return the list of good strings
    return good_strings

def is_good_substring(s):
    # Initialize variables
    num_zeroes = 0
    num_ones = 0
    
    # Iterate through the substring
    for c in s:
        # Check if the current character is a zero or a one
        if c == '0':
            num_zeroes += 1
        elif c == '1':
            num_ones += 1
    
    # Return True if the substring is good, False otherwise
    return num_zeroes != num_ones

def main():
    # Read the input
    n = int(input())
    s = input()
    
    # Cut the string into good substrings
    good_strings = cut_string(s)
    
    # Print the number of good substrings
    print(len(good_strings))
    
    # Print the good substrings
    for s in good_strings:
        print(s, end=' ')

if __name__ == '__main__':
    main()

