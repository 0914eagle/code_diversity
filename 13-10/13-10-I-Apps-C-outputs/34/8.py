
def get_palindromic_strings(s, n):
    # Initialize a list to store the palindromic strings
    palindromic_strings = []
    
    # Iterate over the length of the string
    for i in range(len(s)):
        # Get the substring starting from the current index and having length equal to the remaining length of the string
        substring = s[i:i+n-i]
        
        # Check if the substring is palindromic
        if substring == substring[::-1]:
            # If it is, add it to the list of palindromic strings
            palindromic_strings.append(substring)
    
    # Return the list of palindromic strings
    return palindromic_strings

def count_palindromic_strings(s, n):
    # Get the list of palindromic strings
    palindromic_strings = get_palindromic_strings(s, n)
    
    # Initialize a counter to store the number of palindromic strings
    count = 0
    
    # Iterate over the list of palindromic strings
    for string in palindromic_strings:
        # Check if the string is a subsequence of the input string
        if string in s:
            # If it is, increment the counter
            count += 1
    
    # Return the counter modulo 10^9+7
    return count % 1000000007

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(count_palindromic_strings(s, n))

