
def f1(n, k, a):
    # Initialize variables
    segments = 0
    xor_sum = 0
    
    # Iterate through the array
    for i in range(n):
        # Calculate the XOR sum of the current segment
        xor_sum ^= a[i]
        
        # If the XOR sum is not equal to 0, increment the number of segments
        if xor_sum != 0:
            segments += 1
    
    # Return the maximum number of segments
    return segments

def f2(n, k, a):
    # Initialize variables
    segments = 0
    xor_sum = 0
    
    # Iterate through the array
    for i in range(n):
        # Calculate the XOR sum of the current segment
        xor_sum ^= a[i]
        
        # If the XOR sum is not equal to 0, increment the number of segments
        if xor_sum != 0:
            segments += 1
    
    # Return the maximum number of segments
    return segments

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(n, k, a))
    print(f2(n, k, a))

