
def get_input():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    return H, N, A

def can_raccoon_win(H, N, A):
    # Initialize a set to store the moves that have been used
    used_moves = set()
    # Initialize a variable to store the current health of the monster
    current_health = H
    # Loop through each move
    for i in range(N):
        # If the current health of the monster is 0 or below, return True
        if current_health <= 0:
            return True
        # If the current move has been used before, return False
        if i in used_moves:
            return False
        # Use the current move to decrease the health of the monster
        current_health -= A[i]
        # Add the current move to the set of used moves
        used_moves.add(i)
    # If the loop completes and the current health of the monster is still positive, return False
    return False

def main():
    H, N, A = get_input()
    if can_raccoon_win(H, N, A):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

