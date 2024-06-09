
def solve(n, x):
    # Sort the chips by their coordinates
    x.sort()
    
    # Initialize the minimum number of coins to move all chips to the same coordinate as infinity
    min_coins = float('inf')
    
    # Loop through all possible coordinates
    for i in range(min(x), max(x) + 1):
        # Initialize the number of coins to move chips to the current coordinate as 0
        coins = 0
        
        # Loop through all chips
        for j in range(n):
            # If the coordinate of the current chip is not equal to the current coordinate, we need to move the chip
            if x[j] != i:
                # If the difference between the coordinate of the current chip and the current coordinate is even, we can move the chip by 2 in the direction of the current coordinate for free
                if (x[j] - i) % 2 == 0:
                    x[j] += 2
                # Otherwise, we need to move the chip by 1 in the direction of the current coordinate and pay 1 coin
                else:
                    x[j] += 1
                    coins += 1
        
        # If the number of coins to move chips to the current coordinate is less than or equal to the minimum number of coins, update the minimum number of coins
        if coins <= min_coins:
            min_coins = coins
    
    # Return the minimum number of coins to move all chips to the same coordinate
    return min_coins

