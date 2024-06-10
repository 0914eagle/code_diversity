
def get_minimum_pieces(A, B):
    # Find the smaller of the two numbers
    smaller = min(A, B)
    # Find the larger of the two numbers
    larger = max(A, B)
    # Initialize the minimum number of pieces to the larger number
    min_pieces = larger
    # Loop through all possible numbers of pieces from 1 to the smaller number
    for i in range(1, smaller + 1):
        # Check if the smaller number is divisible by the current number of pieces
        if smaller % i == 0:
            # If it is, calculate the number of pieces that would be left over for the larger number
            leftover = larger - i * (smaller // i)
            # If the number of pieces left over is less than the current minimum, update the minimum
            if leftover < min_pieces:
                min_pieces = leftover
    # Return the minimum number of pieces
    return min_pieces

def main():
    # Read the input from stdin
    A, B = map(int, input().split())
    # Call the function and print the result
    print(get_minimum_pieces(A, B))

if __name__ == '__main__':
    main()

