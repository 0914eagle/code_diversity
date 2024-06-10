
def get_palindromic_strings(S, N):
    # Initialize a list to store the palindromic strings
    palindromic_strings = []
    
    # Iterate over the length of the input string
    for i in range(N):
        # Get the substring starting from the current index and ending at the end of the string
        substring = S[i:]
        
        # Check if the substring is palindromic
        if substring == substring[::-1]:
            # If it is, add it to the list of palindromic strings
            palindromic_strings.append(substring)
    
    # Return the list of palindromic strings
    return palindromic_strings

def count_palindromic_strings(S, N):
    # Get the list of palindromic strings
    palindromic_strings = get_palindromic_strings(S, N)
    
    # Initialize a variable to store the count of palindromic strings
    count = 0
    
    # Iterate over the list of palindromic strings
    for string in palindromic_strings:
        # Check if the string is a subsequence of the input string
        if string in S:
            # If it is, increment the count
            count += 1
    
    # Return the count modulo 10^9+7
    return count % 1000000007

if __name__ == '__main__':
    # Get the input string
    N = int(input())
    S = input()
    
    # Call the function to count the palindromic strings
    count = count_palindromic_strings(S, N)
    
    # Print the result
    print(count)

