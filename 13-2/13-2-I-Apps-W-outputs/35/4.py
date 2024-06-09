
def get_maximum_segments(arr, k):
    # Initialize variables
    n = len(arr)
    segments = 0
    xor_sum = 0
    
    # Iterate through the array
    for i in range(n):
        # Calculate the XOR sum of the current segment
        xor_sum ^= arr[i]
        
        # If the XOR sum is not equal to 0, increment the number of segments
        if xor_sum != 0:
            segments += 1
        
        # If we are at the end of the array, break
        if i == n-1:
            break
        
        # Calculate the XOR sum of the next segment
        next_xor_sum = xor_sum ^ arr[i+1]
        
        # If the XOR sum is not equal to 0, increment the number of segments
        if next_xor_sum != 0:
            segments += 1
        
        # Update the XOR sum for the next iteration
        xor_sum = next_xor_sum
    
    # Return the maximum number of segments
    return segments

def main():
    # Read the input
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Call the function to get the maximum number of segments
    segments = get_maximum_segments(arr, k)
    
    # Print the result
    print(segments)

if __name__ == '__main__':
    main()

