
def f1(N, K, healths):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    monsters_alive = N

    # Sort the healths in descending order
    healths.sort(reverse=True)

    # Loop through the healths and attack the monsters
    for i in range(N):
        # If the current monster's health is 1, use special move
        if healths[i] == 1:
            special_move_count += 1
            monsters_alive -= 1
        # Otherwise, attack the monster
        else:
            attack_count += 1
            healths[i] -= 1
            monsters_alive -= 1

        # If all monsters are dead, break the loop
        if monsters_alive == 0:
            break

    # Return the minimum number of attacks needed
    return attack_count + special_move_count

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, K = map(int, input().split())
    healths = list(map(int, input().split()))
    print(f1(N, K, healths))

