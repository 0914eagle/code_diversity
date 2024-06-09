
def get_min_attacks(N, K, healths):
    # Initialize variables
    min_attacks = float('inf')
    special_moves = K
    attack_count = 0

    # Sort the healths in descending order
    healths.sort(reverse=True)

    # Loop through each monster and attack it
    for i in range(N):
        # If the monster's health is 0, skip it
        if healths[i] == 0:
            continue

        # If the special moves are exhausted, attack the monster
        if special_moves == 0:
            healths[i] -= 1
            attack_count += 1
        # Else, use the special move on the monster
        else:
            special_moves -= 1
            healths[i] = 0

        # If all the monsters are dead, break the loop
        if sum(healths) == 0:
            break

    # Return the minimum number of attacks needed to win
    return attack_count

def main():
    N, K = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(N, K, healths))

if __name__ == '__main__':
    main()

