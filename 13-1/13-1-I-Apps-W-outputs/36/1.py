
def solve(N, D, A, X_H):
    # Sort the monsters by their coordinates
    X_H.sort(key=lambda x: x[0])
    
    # Initialize the number of bombs needed to 0
    bombs_needed = 0
    
    # Loop through the monsters
    for i in range(N):
        # Get the current monster's coordinate and health
        x, h = X_H[i]
        
        # If the monster's health is already 0 or below, skip it
        if h <= 0:
            continue
        
        # Calculate the range of coordinates that the bomb can affect
        range_start = max(x - D, 0)
        range_end = min(x + D, 10**9)
        
        # Calculate the number of monsters that the bomb can affect
        num_monsters = sum(1 for x, h in X_H[i:] if range_start <= x <= range_end)
        
        # Calculate the total health that the bomb can decrease
        total_health = num_monsters * A
        
        # If the total health is greater than the monster's current health, set the health to 0
        if total_health > h:
            total_health = h
        
        # Subtract the total health from the monster's current health
        h -= total_health
        
        # If the monster's health is now 0 or below, increment the number of bombs needed
        if h <= 0:
            bombs_needed += 1
    
    return bombs_needed

