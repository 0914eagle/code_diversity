
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as infinity
    min_time = float('inf')
    
    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the number of manapoints spent as 0
        mana_spent = 0
        # Initialize the number of potions prepared as 0
        potions_prepared = 0
        # Initialize the preparation time as x
        preparation_time = x
        
        # Loop through all m spells
        for j in range(m):
            # Check if the j-th spell is used in the current combination
            if i & (1 << j):
                # Add the mana cost of the spell to the total mana spent
                mana_spent += b[j]
                # Change the preparation time to a[j]
                preparation_time = a[j]
        
        # Loop through all k spells
        for j in range(k):
            # Check if the j-th spell is used in the current combination
            if i & (1 << (m + j)):
                # Add the mana cost of the spell to the total mana spent
                mana_spent += d[j]
                # Add the number of potions created by the spell to the total number of potions prepared
                potions_prepared += c[j]
        
        # Check if the total mana spent is less than or equal to s and the number of potions prepared is greater than or equal to n
        if mana_spent <= s and potions_prepared >= n:
            # Calculate the total time spent on preparing the potions
            total_time = preparation_time * (n - potions_prepared) + potions_prepared * preparation_time
            # Update the minimum time if the total time is less than the current minimum time
            min_time = min(min_time, total_time)
    
    # Return the minimum time
    return min_time

