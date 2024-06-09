
def get_min_attacks(N, K, healths):
    # Initialize variables
    min_attacks = float('inf')
    special_move_count = 0
    attack_count = 0

    # Sort the healths in descending order
    healths.sort(reverse=True)

    # Loop through the healths and calculate the minimum number of attacks
    for i in range(N):
        # If the current health is greater than or equal to the previous health,
        # then we can use the special move
        if healths[i] >= healths[i-1]:
            special_move_count += 1
            healths[i] = 0
        # Otherwise, we need to do an attack
        else:
            attack_count += 1
            healths[i] -= 1

        # If we have used up all our special moves,
        # then we need to do an attack on the next monster
        if special_move_count == K:
            special_move_count = 0
            attack_count += 1

        # Update the minimum number of attacks
        min_attacks = min(min_attacks, attack_count)

    return min_attacks

def main():
    N, K = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(N, K, healths))

if __name__ == '__main__':
    main()

