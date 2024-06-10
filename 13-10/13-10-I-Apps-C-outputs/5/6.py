
def get_num_supported_stewards(n, strengths):
    # Sort the strengths in ascending order
    strengths.sort()
    
    # Initialize variables to keep track of the number of stewards supported and the current index
    num_supported = 0
    index = 0
    
    # Loop through each steward and check if they have a steward with strength less than them and a steward with strength greater than them
    for strength in strengths:
        # If there is a steward with strength less than the current steward, increment the number of supported stewards
        if index > 0 and strengths[index - 1] < strength:
            num_supported += 1
        # If there is a steward with strength greater than the current steward, increment the number of supported stewards
        if index < n - 1 and strengths[index + 1] > strength:
            num_supported += 1
        # Increment the index
        index += 1
    
    # Return the number of supported stewards
    return num_supported

def main():
    # Read the number of stewards and their strengths from stdin
    n = int(input())
    strengths = list(map(int, input().split()))
    
    # Call the function to get the number of supported stewards
    num_supported = get_num_supported_stewards(n, strengths)
    
    # Print the number of supported stewards
    print(num_supported)

if __name__ == '__main__':
    main()

