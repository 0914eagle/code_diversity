
def get_palindromic_strings(n, s):
    # Initialize a list to store the palindromic strings
    palindromic_strings = []
    
    # Iterate over the length of the input string
    for i in range(len(s)):
        # Get the substring starting from the current index and ending at the end of the string
        substring = s[i:]
        
        # Check if the substring is palindromic
        if substring == substring[::-1]:
            # If it is, add it to the list of palindromic strings
            palindromic_strings.append(substring)
    
    # Return the list of palindromic strings
    return palindromic_strings

def get_substring_count(n, s, m):
    # Initialize a counter variable to keep track of the number of palindromic substrings
    count = 0
    
    # Iterate over the length of the input string
    for i in range(len(s)):
        # Get the substring starting from the current index and ending at the end of the string
        substring = s[i:]
        
        # Check if the substring is palindromic
        if substring == substring[::-1]:
            # If it is, increment the counter
            count += 1
    
    # Return the count modulo 10^9+7
    return count % (10**9+7)

def main():
    # Read the input data
    n = int(input())
    s = input()
    
    # Get the list of palindromic strings
    palindromic_strings = get_palindromic_strings(n, s)
    
    # Get the count of palindromic substrings
    count = get_substring_count(n, s, len(palindromic_strings))
    
    # Print the result
    print(count)

if __name__ == '__main__':
    main()

