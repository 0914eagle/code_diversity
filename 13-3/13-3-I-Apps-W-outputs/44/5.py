
def get_max_cuts(n, B, a):
    # Sort the array in non-decreasing order
    a.sort()
    
    # Initialize the maximum number of cuts to 0
    max_cuts = 0
    
    # Loop through the array and check if the current element is a cut
    for i in range(n - 1):
        # Check if the current element is a cut
        if a[i] % 2 == 0 and a[i + 1] % 2 == 1:
            # Calculate the cost of the cut
            cost = abs(a[i] - a[i + 1])
            
            # Check if the cost is less than or equal to the budget
            if cost <= B:
                # Increment the maximum number of cuts
                max_cuts += 1
                
                # Decrement the budget by the cost of the cut
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

