
def f1(N, K, healths):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    monsters_alive = N

    # Sort the healths in descending order
    healths.sort(reverse=True)

    # Loop through the healths and attack the monsters
    for i in range(N):
        # If the current monster's health is 0, skip it
        if healths[i] == 0:
            continue

        # If the current monster's health is 1 and Special Move is available, use Special Move
        if healths[i] == 1 and special_move_count < K:
            special_move_count += 1
            healths[i] = 0
            monsters_alive -= 1
        else:
            # Otherwise, attack the monster
            healths[i] -= 1
            attack_count += 1

            # If the current monster's health becomes 0, remove it from the game
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

