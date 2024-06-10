
def get_supported_stewards(stewards):
    # Sort the stewards in non-decreasing order
    stewards.sort()
    
    # Initialize the number of supported stewards to 0
    supported_stewards = 0
    
    # Iterate through the stewards
    for i in range(len(stewards)):
        # Check if there is a steward with strength less than the current steward
        if i > 0 and stewards[i] > stewards[i-1]:
            # Increment the number of supported stewards
            supported_stewards += 1
    
    # Return the number of supported stewards
    return supported_stewards

def main():
    # Read the number of stewards
    n = int(input())
    
    # Read the strengths of the stewards
    stewards = list(map(int, input().split()))
    
    # Call the get_supported_stewards function
    supported_stewards = get_supported_stewards(stewards)
    
    # Print the number of supported stewards
    print(supported_stewards)

if __name__ == '__main__':
    main()

