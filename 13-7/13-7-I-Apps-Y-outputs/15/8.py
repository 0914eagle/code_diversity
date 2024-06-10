
def get_strings(n, k):
    # Initialize an empty list to store the strings
    strings = []
    
    # Iterate over all possible strings of length n
    for i in range(n):
        for j in range(i+1, n):
            # Check if the string contains n-2 letters 'a' and two letters 'b'
            if n - (i + j) == 2:
                # Add the string to the list
                strings.append(chr(i + 97) + chr(j + 97))
    
    # Return the k-th string from the list
    return strings[k-1]

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over each test case
    for i in range(t):
        # Read the values of n and k
        n, k = map(int, input().split())
        
        # Call the get_strings function to get the k-th string
        string = get_strings(n, k)
        
        # Print the string
        print(string)

if __name__ == '__main__':
    main()

