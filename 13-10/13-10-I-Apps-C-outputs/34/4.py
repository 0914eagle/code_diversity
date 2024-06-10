
def get_palindromic_strings(s, n):
    # Initialize a list to store the palindromic strings
    palindromic_strings = []
    
    # Loop through each substring of length 2n in s
    for i in range(len(s)):
        # Check if the substring is palindromic
        if s[i:i+n] == s[i:i+n][::-1]:
            # If it is, add it to the list of palindromic strings
            palindromic_strings.append(s[i:i+n])
    
    # Return the list of palindromic strings
    return palindromic_strings

def count_palindromic_strings(s, n):
    # Get the list of palindromic strings of length 2n that contain s as a subsequence
    palindromic_strings = get_palindromic_strings(s, n)
    
    # Count the number of palindromic strings in the list
    count = len(palindromic_strings)
    
    # Return the count modulo 10^9 + 7
    return count % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(count_palindromic_strings(s, n))

