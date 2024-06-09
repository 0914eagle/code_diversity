
def get_input():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    return H, N, A

def can_win(H, N, A):
    # Initialize a set to keep track of the moves that have been used
    used_moves = set()
    # Initialize a variable to keep track of the current health of the monster
    current_health = H
    # Loop through each move and check if it can be used to win the game
    for i in range(N):
        # If the move has already been used, skip it
        if i in used_moves:
            continue
        # Calculate the new health of the monster after using the current move
        new_health = current_health - A[i]
        # If the new health is 0 or below, return True
        if new_health <= 0:
            return True
        # Add the current move to the set of used moves
        used_moves.add(i)
        # Set the current health to the new health
        current_health = new_health
    # If all moves have been used and the monster's health is still above 0, return False
    return False

def main():
    H, N, A = get_input()
    print("Yes") if can_win(H, N, A) else print("No")

if __name__ == '__main__':
    main()

