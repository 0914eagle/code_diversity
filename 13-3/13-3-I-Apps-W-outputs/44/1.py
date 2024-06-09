
def get_max_cuts(n, B, a):
    # Sort the array in non-decreasing order
    a.sort()
    
    # Initialize the maximum number of cuts to 0
    max_cuts = 0
    
    # Loop through each element in the array
    for i in range(n - 1):
        # Calculate the cost of the current cut
        cost = abs(a[i] - a[i + 1])
        
        # Check if the current cut is within the budget
        if cost <= B:
            # Increment the maximum number of cuts
            max_cuts += 1
            # Decrement the budget by the cost of the current cut
            B -= cost
    
    # Return the maximum number of cuts
    return max_cuts

def main():
    # Read the input n, B, and a from stdin
    n, B = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_max_cuts function and print the result
    print(get_max_cuts(n, B, a))

if __name__ == '__main__':
    main()

