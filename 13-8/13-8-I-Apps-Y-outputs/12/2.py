
def get_minimum_moves(a, k):
    # Initialize variables
    x = 0
    moves = 0
    n = len(a)
    
    # Loop through each element of the array
    for i in range(n):
        # Check if the current element is not divisible by k
        if a[i] % k != 0:
            # Calculate the number of moves required to make the element divisible by k
            moves += (a[i] // k) + 1
            # Increase the current element by the number of moves
            a[i] += moves
    
    # Return the total number of moves required
    return moves

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        # Call the get_minimum_moves function and print the result
        print(get_minimum_moves(a, k))

if __name__ == '__main__':
    main()

