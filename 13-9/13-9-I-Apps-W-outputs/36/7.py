
def solve(n, s, t, shuffle_operations):
    # Initialize a list to store the positions of the glasses
    glasses = list(range(1, n+1))
    
    # Initialize a variable to store the minimum number of shuffling operations
    min_operations = 0
    
    # Loop through each shuffling operation
    for p in shuffle_operations:
        # Find the index of the glass that is being shuffled
        index = glasses.index(s)
        
        # Shuffle the glasses
        glasses.insert(p-1, glasses.pop(index))
        
        # Increment the minimum number of shuffling operations
        min_operations += 1
    
    # Return the minimum number of shuffling operations if the marble can move from position s to position t, otherwise return -1
    return min_operations if glasses.index(t) == s-1 else -1

def main():
    # Read the input data
    n, s, t = map(int, input().split())
    shuffle_operations = list(map(int, input().split()))
    
    # Solve the problem
    result = solve(n, s, t, shuffle_operations)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

