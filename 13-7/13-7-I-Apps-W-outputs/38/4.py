
def get_valid_amidakuji(H, W, K):
    # Initialize a list to store the valid amidakuji
    valid_amidakuji = []
    
    # Iterate through all possible vertical lines
    for i in range(1, H+1):
        # Iterate through all possible horizontal lines
        for j in range(1, W+1):
            # Check if the horizontal line is valid
            if j % (i+1) == 0:
                # Add the horizontal line to the valid amidakuji
                valid_amidakuji.append((i, j))
    
    # Return the number of valid amidakuji modulo 1000000007
    return len(valid_amidakuji) % 1000000007

def main():
    # Read the input from stdin
    H, W, K = map(int, input().split())
    
    # Call the function to get the number of valid amidakuji
    result = get_valid_amidakuji(H, W, K)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

