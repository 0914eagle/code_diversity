
def get_input():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    return H, N, A

def solve(H, N, A):
    # Initialize a set to store the moves that have been used
    used_moves = set()
    # Initialize a variable to store the current health of the monster
    current_health = H
    # Loop through each move in the list of moves
    for i in range(N):
        # If the current move has not been used before, use it to decrease the monster's health
        if i not in used_moves:
            current_health -= A[i]
            # Add the current move to the set of used moves
            used_moves.add(i)
        # If the monster's health becomes 0 or below, return True
        if current_health <= 0:
            return True
    # If all moves have been used and the monster's health is still positive, return False
    return False

def main():
    H, N, A = get_input()
    print("Yes") if solve(H, N, A) else print("No")

if __name__ == '__main__':
    main()

