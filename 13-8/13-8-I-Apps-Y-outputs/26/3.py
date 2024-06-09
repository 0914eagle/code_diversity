
def solve(H, n, d):
    # Calculate the total damage dealt by the monster in each round
    total_damage = sum(d)

    # If the total damage is greater than or equal to the initial health,
    # the monster will die in the first round
    if total_damage >= H:
        return 1

    # If the total damage is less than the initial health,
    # the monster will not die in the first round
    else:
        # Calculate the number of rounds needed to kill the monster
        num_rounds = H // total_damage

        # Calculate the number of minutes needed to kill the monster
        num_minutes = num_rounds * n

        # Return the number of minutes needed to kill the monster
        return num_minutes + 1

