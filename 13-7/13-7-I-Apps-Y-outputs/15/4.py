
def get_string(n, k):
    # Initialize an empty list to store the strings
    strings = []
    
    # Iterate over all possible combinations of 'a' and 'b'
    for i in range(n):
        for j in range(i+1, n):
            # Check if the current combination has n-2 'a' and 2 'b'
            if i + j == n - 2:
                # Add the current combination to the list
                strings.append('a' * i + 'b' * (j-i) + 'a' * (n-i-j))
    
    # Return the k-th string from the list
    return strings[k-1]

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over each test case
    for _ in range(t):
        # Read the values of n and k
        n, k = map(int, input().split())
        
        # Call the get_string function to get the k-th string
        string = get_string(n, k)
        
        # Print the string
        print(string)

if __name__ == '__main__':
    main()

