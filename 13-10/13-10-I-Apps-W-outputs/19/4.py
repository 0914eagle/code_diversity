
def get_min_bitwise_or(a, b):
    # Calculate the bitwise AND of a and b
    c = a & b
    
    # Initialize the minimum bitwise OR as the first element of c
    min_or = c[0]
    
    # Loop through the rest of the elements of c
    for i in range(1, len(c)):
        # Calculate the bitwise OR of the current element and the minimum bitwise OR so far
        min_or |= c[i]
    
    return min_or

def main():
    # Read the input data
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Calculate the minimum bitwise OR
    min_or = get_min_bitwise_or(a, b)
    
    # Print the result
    print(min_or)

if __name__ == '__main__':
    main()

