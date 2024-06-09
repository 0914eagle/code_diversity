
def f1(N, K, healths):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    monsters_alive = N
    healths = sorted(healths, reverse=True)

    # Loop through the monsters
    for i in range(N):
        # If the monster's health is 0, skip it
        if healths[i] == 0:
            continue

        # If the special move count is less than K, use the special move
        if special_move_count < K:
            special_move_count += 1
            healths[i] = 0
            monsters_alive -= 1

        # Otherwise, do an attack
        else:
            attack_count += 1
            healths[i] -= 1

            # If the monster's health is 0 after the attack, remove it from the game
            if healths[i] == 0:
                monsters_alive -= 1

    # Return the minimum number of attacks needed to win
    return attack_count

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, K = map(int, input().split())
    healths = list(map(int, input().split()))
    print(f1(N, K, healths))

