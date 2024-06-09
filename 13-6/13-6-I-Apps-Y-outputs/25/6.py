
def solve(N, K, health):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    max_health = max(health)

    # Loop through each monster and attack or special move as needed
    for i in range(N):
        if health[i] == max_health:
            # Special move on the strongest monster
            special_move_count += 1
            health[i] = 0
        else:
            # Attack the monster
            attack_count += 1
            health[i] -= 1

    # Check if Fennec has won
    if all(h == 0 for h in health):
        return attack_count

    # If Fennec has not won, use special move as many times as possible
    while special_move_count < K and any(h > 0 for h in health):
        # Find the strongest monster that is not already dead
        max_health = max(h for h in health if h > 0)

        # Special move on the strongest monster
        special_move_count += 1
        health[health.index(max_health)] = 0

        # Check if Fennec has won
        if all(h == 0 for h in health):
            return attack_count

    # If Fennec has not won, return the number of attacks done so far
    return attack_count + special_move_count

