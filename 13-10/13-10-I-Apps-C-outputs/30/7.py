
import math

def get_max_minions(n, m, r, villages, minions):
    # Calculate the maximum distance between any two points
    max_distance = math.sqrt(2 * r ** 2)
    
    # Initialize a list to store the minimum distance between each minion and its closest village
    min_distances = [float('inf') for _ in range(m)]
    
    # Iterate over each village
    for i in range(n):
        # Get the coordinates and radius of the current village
        vx, vy, vr = villages[i]
        
        # Calculate the distance between the current village and each minion
        for j in range(m):
            mx, my = minions[j]
            distance = math.sqrt((vx - mx) ** 2 + (vy - my) ** 2)
            
            # If the distance is less than the minimum distance, update the minimum distance
            if distance < min_distances[j]:
                min_distances[j] = distance
    
    # Find the minimum distance between any two points
    min_distance = min(min_distances)
    
    # Return the maximum number of minions that can be destroyed
    return int(math.ceil(min_distance / max_distance))

def main():
    n, m, r = map(int, input().split())
    villages = []
    for i in range(n):
        vx, vy, vr = map(int, input().split())
        villages.append((vx, vy, vr))
    minions = []
    for i in range(m):
        mx, my = map(int, input().split())
        minions.append((mx, my))
    print(get_max_minions(n, m, r, villages, minions))

if __name__ == '__main__':
    main()

