
def get_supported_stewards(stewards):
    # Find the minimum and maximum strength values
    min_strength, max_strength = min(stewards), max(stewards)
    
    # Initialize a counter for the number of supported stewards
    supported_stewards = 0
    
    # Iterate over the stewards
    for steward in stewards:
        # Check if there is a steward with a strength less than the current steward
        if any(steward > s for s in stewards):
            supported_stewards += 1
    
    return supported_stewards

def main():
    # Read the number of stewards
    n = int(input())
    
    # Read the strength values of the stewards
    stewards = list(map(int, input().split()))
    
    # Call the get_supported_stewards function
    supported_stewards = get_supported_stewards(stewards)
    
    # Print the number of supported stewards
    print(supported_stewards)

if __name__ == '__main__':
    main()

