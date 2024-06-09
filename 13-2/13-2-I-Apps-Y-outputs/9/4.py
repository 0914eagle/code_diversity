
def solve(n, x):
    # Sort the chips by their coordinates
    x.sort()
    
    # Initialize the minimum number of coins to move all chips to the same coordinate as infinity
    min_coins = float('inf')
    
    # Loop through all possible coordinates
    for coord in x:
        # Initialize the number of coins to move chips to this coordinate as 0
        coins = 0
        
        # Loop through all chips
        for i in range(n):
            # If the chip is not at the current coordinate, calculate the number of coins needed to move it to this coordinate
            if x[i] != coord:
                # If the chip is more than 2 positions away from the current coordinate, move it by 2 positions and pay 1 coin
                if abs(x[i] - coord) > 2:
                    coins += 1
                # If the chip is 2 positions away from the current coordinate, move it by 1 position and pay 1 coin
                elif abs(x[i] - coord) == 2:
                    coins += 1
                # If the chip is 1 position away from the current coordinate, move it by 1 position and pay 0 coins
                elif abs(x[i] - coord) == 1:
                    pass
        
        # If the number of coins needed to move all chips to this coordinate is less than the current minimum, update the minimum
        if coins < min_coins:
            min_coins = coins
    
    # Return the minimum number of coins needed to move all chips to the same coordinate
    return min_coins

