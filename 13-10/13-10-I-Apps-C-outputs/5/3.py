
def find_number_of_supported_stewards(n, steward_strengths):
    # Sort the steward strengths in non-decreasing order
    steward_strengths.sort()
    
    # Initialize the number of supported stewards to 0
    number_of_supported_stewards = 0
    
    # Iterate over the stewards
    for i in range(n):
        # Check if the current steward has a stronger steward to its left and a weaker steward to its right
        if i > 0 and steward_strengths[i] > steward_strengths[i-1] and i < n-1 and steward_strengths[i] < steward_strengths[i+1]:
            # Increment the number of supported stewards
            number_of_supported_stewards += 1
    
    # Return the number of supported stewards
    return number_of_supported_stewards

def main():
    # Read the number of stewards
    n = int(input())
    
    # Read the strengths of the stewards
    steward_strengths = list(map(int, input().split()))
    
    # Find the number of supported stewards
    number_of_supported_stewards = find_number_of_supported_stewards(n, steward_strengths)
    
    # Print the number of supported stewards
    print(number_of_supported_stewards)

if __name__ == '__main__':
    main()

