
def get_input():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    return H, N, A

def solve(H, N, A):
    # Initialize a set to keep track of the moves used
    moves_used = set()
    # Initialize a variable to keep track of the current health
    current_health = H
    # Loop through each move
    for i in range(N):
        # If the current health becomes 0 or below, return "Yes"
        if current_health <= 0:
            return "Yes"
        # If the move has already been used, continue to the next move
        if i in moves_used:
            continue
        # Otherwise, use the move and decrease the current health
        current_health -= A[i]
        # Add the move to the set of moves used
        moves_used.add(i)
    # If all moves have been used and the current health is still positive, return "No"
    if current_health > 0:
        return "No"

if __name__ == '__main__':
    H, N, A = get_input()
    print(solve(H, N, A))

