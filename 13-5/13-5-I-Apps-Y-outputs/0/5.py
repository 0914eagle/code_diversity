
def get_min_attacks(N, K, healths):
    # Initialize variables
    min_attacks = float('inf')
    special_move_count = 0
    healths = sorted(healths, reverse=True)

    # Base case: if all monsters are already dead, return 0
    if sum(healths) == 0:
        return 0

    # Recursive case: try all possible combinations of attacks and special moves
    for i in range(N):
        # Skip if monster is already dead
        if healths[i] == 0:
            continue

        # Try attacking the current monster
        healths[i] -= 1
        attcks = get_min_attacks(N, K, healths)

        # Undo the attack and try special move if possible
        if special_move_count < K:
            healths[i] = 0
            special_move_count += 1
            attcks = min(attcks, get_min_attacks(N, K, healths))

        # Update minimum number of attacks
        min_attacks = min(min_attacks, attcks)

        # Undo the special move if it was tried
        if special_move_count > 0:
            special_move_count -= 1
            healths[i] = 1

    return min_attacks

def main():
    N, K = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(N, K, healths))

if __name__ == '__main__':
    main()

