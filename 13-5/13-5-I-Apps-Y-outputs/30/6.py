
def get_input():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    return H, N, A

def can_raccoon_win(H, N, A):
    # Initialize a set to keep track of the moves used
    moves_used = set()
    # Initialize a variable to keep track of the current health
    current_health = H
    # Loop through each move
    for i in range(N):
        # If the current health becomes 0 or below, return True
        if current_health <= 0:
            return True
        # If the current move has been used before, return False
        if i in moves_used:
            return False
        # Otherwise, decrease the current health by the move's value and add the move to the set of moves used
        current_health -= A[i]
        moves_used.add(i)
    # If all moves have been used and the current health is still positive, return True
    return current_health > 0

def main():
    H, N, A = get_input()
    if can_raccoon_win(H, N, A):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

