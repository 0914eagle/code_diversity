
def get_amidakuji(h, w, k):
    # Initialize a list to store the number of valid amidakuji
    count = 0
    
    # Loop through all possible vertical lines
    for i in range(1, h + 1):
        # Loop through all possible horizontal lines
        for j in range(1, w + 1):
            # Check if the horizontal line is valid
            if i + j <= h and i + j >= 1 and j <= w:
                # Increment the count
                count += 1
    
    # Return the count modulo 1000000007
    return count % 1000000007

def main():
    # Read the input from stdin
    h, w, k = map(int, input().split())
    
    # Call the get_amidakuji function and print the result
    print(get_amidakuji(h, w, k))

if __name__ == '__main__':
    main()

