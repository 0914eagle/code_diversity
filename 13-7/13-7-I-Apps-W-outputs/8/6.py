
def read_input():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for _ in range(H):
        B.append(list(map(int, input().split())))
    return H, W, A, B

def solve(H, W, A, B):
    # Initialize the minimum unbalancedness to a large value
    min_unbalancedness = 1000
    
    # Loop through all possible colorings of the grid
    for i in range(2**(H*W)):
        # Convert the integer into a binary string with H*W digits
        binary_string = bin(i)[2:].zfill(H*W)
        
        # Initialize the sum of red and blue numbers to 0
        red_sum, blue_sum = 0, 0
        
        # Loop through each square in the grid
        for j in range(H*W):
            # If the j-th digit of the binary string is 0, paint the j-th square red
            if binary_string[j] == '0':
                red_sum += A[j//W][j%W]
                blue_sum += B[j//W][j%W]
            # If the j-th digit of the binary string is 1, paint the j-th square blue
            else:
                red_sum += B[j//W][j%W]
                blue_sum += A[j//W][j%W]
        
        # Calculate the unbalancedness for this coloring
        unbalancedness = abs(red_sum - blue_sum)
        
        # Update the minimum unbalancedness if necessary
        if unbalancedness < min_unbalancedness:
            min_unbalancedness = unbalancedness
    
    # Return the minimum unbalancedness
    return min_unbalancedness

def main():
    H, W, A, B = read_input()
    print(solve(H, W, A, B))

if __name__ == '__main__':
    main()

