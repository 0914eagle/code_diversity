
def get_min_attacks(healths, k):
    # Initialize variables
    attacks = 0
    special_moves = k
    monsters_alive = len(healths)

    # Sort the healths in descending order
    healths.sort(reverse=True)

    # Loop through the healths and attack the monsters
    for i in range(len(healths)):
        # If the current monster's health is 1, use a special move to kill it
        if healths[i] == 1:
            special_moves -= 1
            monsters_alive -= 1
        # Otherwise, attack the monster and decrease its health by 1
        else:
            healths[i] -= 1
            attacks += 1
            monsters_alive -= 1

        # If all monsters are killed, return the number of attacks
        if monsters_alive == 0:
            return attacks

    # If all special moves are used, return -1 to indicate that Fennec cannot win
    if special_moves == 0:
        return -1

    # If there are still monsters alive and special moves left, continue attacking
    return get_min_attacks(healths, special_moves)

def main():
    n, k = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(healths, k))

if __name__ == '__main__':
    main()

