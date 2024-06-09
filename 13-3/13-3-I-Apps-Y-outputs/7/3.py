
def get_min_moves(a, b):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Loop through all possible values of k from 1 to 10
    for k in range(1, 11):
        # If a + k == b, we have found the minimum number of moves
        if a + k == b:
            return 1
        # If a - k == b, we have found the minimum number of moves
        if a - k == b:
            return 1
        # Otherwise, recurse with a + k and a - k as the new values of a
        min_moves = min(min_moves, get_min_moves(a + k, b))
        min_moves = min(min_moves, get_min_moves(a - k, b))
    # Return the minimum number of moves
    return min_moves

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(get_min_moves(a, b))

if __name__ == '__main__':
    main()

