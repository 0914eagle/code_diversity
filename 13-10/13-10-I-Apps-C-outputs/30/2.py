
import math

def get_max_minions(n, m, r, villages, minions):
    # Calculate the maximum radius of the attack
    max_radius = math.sqrt(r**2 - (vx**2 + vy**2))
    
    # Initialize a set to store the minions that can be destroyed
    destroyable_minions = set()
    
    # Loop through each minion
    for minion in minions:
        # Calculate the distance between the minion and the center of the attack
        distance = math.sqrt((minion[0] - vx)**2 + (minion[1] - vy)**2)
        
        # If the minion is within the attack radius, add it to the set of destroyable minions
        if distance <= max_radius:
            destroyable_minions.add(minion)
    
    # Return the number of destroyable minions
    return len(destroyable_minions)

def main():
    # Read the input
    n, m, r = map(int, input().split())
    villages = []
    for _ in range(n):
        vx, vy, vr = map(int, input().split())
        villages.append((vx, vy, vr))
    minions = []
    for _ in range(m):
        mx, my = map(int, input().split())
        minions.append((mx, my))
    
    # Calculate the maximum number of minions that can be destroyed
    max_minions = 0
    for village in villages:
        vx, vy, vr = village
        destroyable_minions = get_max_minions(n, m, r, villages, minions, (vx, vy, vr))
        max_minions = max(max_minions, destroyable_minions)
    
    # Print the output
    print(max_minions)

if __name__ == '__main__':
    main()

