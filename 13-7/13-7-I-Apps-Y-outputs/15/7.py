
def get_string(n, k):
    # Initialize a list to store the strings
    strings = []
    
    # Iterate over all possible strings of length n
    for i in range(n):
        for j in range(i+1, n):
            # Check if the string contains n-2 'a' and 2 'b'
            if (n-2)*'a' + 2*'b' == i*'a' + (j-i)*'b':
                # Add the string to the list
                strings.append(i*'a' + (j-i)*'b')
    
    # Return the k-th string from the list
    return strings[k-1]

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over each test case
    for _ in range(t):
        # Read the input n and k
        n, k = map(int, input().split())
        
        # Get the k-th string
        string = get_string(n, k)
        
        # Print the string
        print(string)

if __name__ == '__main__':
    main()

