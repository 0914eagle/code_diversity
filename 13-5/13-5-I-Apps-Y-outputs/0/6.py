
def get_min_attacks(healths, k):
    # Initialize variables
    num_attacks = 0
    num_special_moves = k
    healths = sorted(healths, reverse=True)

    # Loop through the monsters and attack or use special move as needed
    while healths[0] > 0:
        if num_special_moves > 0 and healths[0] > healths[1]:
            # Use special move on the strongest monster
            healths[0] = 0
            num_special_moves -= 1
        else:
            # Attack the strongest monster
            healths[0] -= 1
            num_attacks += 1

        # Sort the monsters by health in descending order
        healths = sorted(healths, reverse=True)

    return num_attacks

def main():
    num_monsters, num_special_moves = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(healths, num_special_moves))

if __name__ == '__main__':
    main()

