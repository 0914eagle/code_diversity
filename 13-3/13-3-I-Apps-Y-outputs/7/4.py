
def get_min_moves(a, b):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Loop through all possible values of k from 1 to 10
    for k in range(1, 11):
        # If a + k or a - k is equal to b, return the current number of moves
        if a + k == b or a - k == b:
            return min_moves
        # Otherwise, update the minimum number of moves and continue the loop
        min_moves = min(min_moves, 1)
    # If no value of k leads to b, return the minimum number of moves
    return min_moves

def main():
    # Read the number of test cases
    t = int(input())
    # Loop through each test case
    for _ in range(t):
        # Read the input a and b
        a, b = map(int, input().split())
        # Get the minimum number of moves to obtain b from a
        min_moves = get_min_moves(a, b)
        # Print the result
        print(min_moves)

if __name__ == '__main__':
    main()

