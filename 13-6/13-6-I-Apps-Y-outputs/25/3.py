
def solve(N, K, health):
    # Calculate the minimum number of attacks needed to kill all monsters
    min_attacks = sum(health)

    # If Fennec can use Special Move, calculate the minimum number of attacks needed to kill all monsters with Special Move
    if K > 0:
        min_attacks = min(min_attacks, sum(health) - K * max(health))

    return min_attacks

