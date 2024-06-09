
def is_winnable(health, moves):
    # Initialize a set to keep track of the moves that have been used
    used_moves = set()
    # Initialize the current health of the monster
    current_health = health
    # Loop through the moves and try to use each one
    for move in moves:
        # If the move has already been used, return False
        if move in used_moves:
            return False
        # Use the move to decrease the monster's health
        current_health -= move
        # If the monster's health becomes 0 or below, return True
        if current_health <= 0:
            return True
        # Add the move to the set of used moves
        used_moves.add(move)
    # If all moves have been used and the monster's health is still positive, return False
    return False

def main():
    health, num_moves = map(int, input().split())
    moves = list(map(int, input().split()))
    print("Yes") if is_winnable(health, moves) else print("No")

if __name__ == '__main__':
    main()

