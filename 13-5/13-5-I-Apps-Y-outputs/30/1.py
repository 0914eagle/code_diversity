
def get_input():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    return H, N, A

def check_win(H, N, A):
    # Initialize a set to store the moves that have been used
    used_moves = set()
    # Initialize a variable to store the current health of the monster
    current_health = H
    # Loop through each move
    for i in range(N):
        # If the move has not been used before, use it and decrease the current health
        if i not in used_moves:
            current_health -= A[i]
            # If the current health becomes 0 or below, return True
            if current_health <= 0:
                return True
            # Add the move to the set of used moves
            used_moves.add(i)
    # If all moves have been used and the current health is still above 0, return False
    return False

def main():
    H, N, A = get_input()
    print("Yes") if check_win(H, N, A) else print("No")

if __name__ == '__main__':
    main()

