
def find_supported_stewards(n, strengths):
    # Sort the strengths in ascending order
    strengths.sort()
    
    # Initialize the number of supported stewards to 0
    supported_stewards = 0
    
    # Iterate through the strengths
    for i in range(n):
        # Check if there is a steward with strength less than the current steward
        if i > 0 and strengths[i] > strengths[i - 1]:
            # Increment the number of supported stewards
            supported_stewards += 1
        # Check if there is a steward with strength greater than the current steward
        if i < n - 1 and strengths[i] < strengths[i + 1]:
            # Increment the number of supported stewards
            supported_stewards += 1
    
    # Return the number of supported stewards
    return supported_stewards

def main():
    # Read the number of stewards and their strengths from stdin
    n = int(input())
    strengths = list(map(int, input().split()))
    
    # Call the find_supported_stewards function and print the result
    print(find_supported_stewards(n, strengths))

if __name__ == '__main__':
    main()

