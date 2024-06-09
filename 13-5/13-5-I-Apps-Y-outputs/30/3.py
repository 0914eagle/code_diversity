
def can_raccoon_win(health, moves):
    # Initialize a set to keep track of the moves already used
    used_moves = set()
    
    # Loop through each move and check if the monster's health becomes 0 or below
    for move in moves:
        if health - move < 0:
            return "Yes"
        health -= move
        used_moves.add(move)
    
    # If the monster's health is not 0 or below after all moves, return "No"
    if health > 0:
        return "No"
    
    # If the monster's health is 0 or below after all moves, check if all moves have been used
    if len(used_moves) == len(moves):
        return "Yes"
    else:
        return "No"

def main():
    health, num_moves = map(int, input().split())
    moves = list(map(int, input().split()))
    print(can_raccoon_win(health, moves))

if __name__ == '__main__':
    main()

