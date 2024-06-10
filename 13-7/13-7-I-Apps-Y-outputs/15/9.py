
def get_string(n, k):
    # Initialize a list to store the strings
    strings = []
    
    # Iterate over all possible combinations of 'a' and 'b'
    for i in range(n):
        for j in range(n):
            if i + j == n - 2:
                # If the combination has the correct number of 'a' and 'b', add it to the list
                strings.append('a' * i + 'b' * j)
    
    # Sort the list lexicographically
    strings.sort()
    
    # Return the k-th string from the list
    return strings[k - 1]

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over the test cases
    for _ in range(t):
        # Read the input
        n, k = map(int, input().split())
        
        # Get the k-th string from the list
        string = get_string(n, k)
        
        # Print the string
        print(string)

if __name__ == '__main__':
    main()

