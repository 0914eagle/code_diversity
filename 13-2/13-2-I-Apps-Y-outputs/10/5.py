
def f1(N, K, healths):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    monsters_alive = N
    healths = sorted(healths, reverse=True)

    # Loop through the monsters and attack them
    for i in range(N):
        # If Fennec has used all her special moves, she can only attack
        if special_move_count == K:
            attack_count += 1
            healths[i] -= 1
        # If Fennec has not used all her special moves, she can use a special move
        else:
            special_move_count += 1
            healths[i] = 0

        # Check if all monsters are dead
        if sum(healths) == 0:
            break

    # Return the minimum number of attacks needed to win
    return attack_count

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, K = map(int, input().split())
    healths = list(map(int, input().split()))
    print(f1(N, K, healths))

