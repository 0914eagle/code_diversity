
def get_min_attacks(healths, k):
    # Initialize variables
    num_attacks = 0
    num_special_moves = k
    monsters_alive = len(healths)
    healths = sorted(healths, reverse=True)
    
    # Loop through the monsters and attack or use special move as needed
    while monsters_alive > 0:
        if num_special_moves > 0 and healths[0] > 1:
            healths[0] = 1
            num_special_moves -= 1
        else:
            healths[0] -= 1
            num_attacks += 1
        if healths[0] <= 0:
            healths.pop(0)
            monsters_alive -= 1
    
    # Return the minimum number of attacks needed
    return num_attacks

def main():
    num_monsters, k = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(healths, k))

if __name__ == '__main__':
    main()

