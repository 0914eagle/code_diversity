
def get_min_attacks(healths, k):
    # Initialize variables
    attacks = 0
    special_moves = k
    monsters_alive = len(healths)
    healths = sorted(healths, reverse=True)
    
    # Loop through the monsters and attack or use special move
    while monsters_alive > 0:
        if special_moves > 0:
            # Use special move on the current monster
            healths[0] = 0
            special_moves -= 1
        else:
            # Attack the current monster
            healths[0] -= 1
            attacks += 1
        
        # Remove the current monster if its health is 0
        if healths[0] == 0:
            healths.pop(0)
            monsters_alive -= 1
    
    return attacks

def main():
    n, k = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(healths, k))

if __name__ == '__main__':
    main()

