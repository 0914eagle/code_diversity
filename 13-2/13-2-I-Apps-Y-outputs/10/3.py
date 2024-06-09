
def f1(N, K, healths):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    monsters_alive = N

    # Sort the healths in descending order
    healths.sort(reverse=True)

    # Loop through the healths and apply attacks and special moves
    for i in range(N):
        if healths[i] > 0:
            if special_move_count < K:
                special_move_count += 1
                healths[i] = 0
            else:
                attack_count += 1
                healths[i] -= 1

            if healths[i] <= 0:
                monsters_alive -= 1
                if monsters_alive == 0:
                    break

    return attack_count

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, K = map(int, input().split())
    healths = list(map(int, input().split()))
    print(f1(N, K, healths))

