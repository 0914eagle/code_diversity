
def solve(N, K, health):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    health_sum = sum(health)

    # Sort the health array in descending order
    health.sort(reverse=True)

    # Loop through the health array and check if Fennec can win with each monster
    for i in range(N):
        # If Fennec can win with the current monster, return the attack count
        if health[i] <= attack_count:
            return attack_count

        # If Fennec can use Special Move on the current monster, use it and increment the special move count
        if special_move_count < K and health[i] <= health_sum - health[i]:
            special_move_count += 1
            health_sum -= health[i]
        else:
            # Otherwise, do an Attack and increment the attack count
            attack_count += 1
            health_sum -= 1

    # If Fennec cannot win with any monster, return -1
    return -1

