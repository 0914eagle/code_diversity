
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as infinity
    min_time = float('inf')

    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the number of potions prepared and the total mana spent
        num_potions = 0
        total_mana = 0

        # Loop through all spells
        for j in range(m):
            # Check if the j-th spell is used in the current combination
            if i & (1 << j):
                # Add the number of potions created by the j-th spell to the total
                num_potions += c[j]

                # Check if the j-th spell is of the first type
                if b[j] != 0:
                    # Add the mana cost of the j-th spell to the total
                    total_mana += b[j]

        # Check if the total mana spent is less than or equal to the maximum allowed
        if total_mana <= s:
            # Calculate the total time to prepare the potions
            total_time = x * (n - num_potions)

            # Loop through all spells
            for j in range(m):
                # Check if the j-th spell is used in the current combination
                if i & (1 << j):
                    # Add the time saved by the j-th spell to the total
                    total_time += a[j] * c[j]

            # Update the minimum time if the current combination is faster
            min_time = min(min_time, total_time)

    # Return the minimum time to prepare n potions
    return min_time

