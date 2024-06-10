
import math

def get_attack_radius(radius, villages):
    # Calculate the minimum radius needed to destroy all minions without damaging any villages
    min_radius = math.inf
    for village in villages:
        min_radius = min(min_radius, math.sqrt((village[0] ** 2) + (village[1] ** 2)))
    
    # Return the maximum between the minimum radius and the given radius
    return max(min_radius, radius)

def get_attack_area(center, radius):
    # Calculate the area of the attack circle
    area = math.pi * radius ** 2
    
    # Return the area
    return area

def get_minions_destroyed(minions, attack_area):
    # Initialize a counter for the number of minions destroyed
    destroyed = 0
    
    # Iterate over the minions and check if they are within the attack area
    for minion in minions:
        if get_distance(minion, center) <= radius:
            destroyed += 1
    
    # Return the number of minions destroyed
    return destroyed

def get_distance(point1, point2):
    # Calculate the distance between the two points
    distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    
    # Return the distance
    return distance

def main():
    # Read the input
    n, m, r = map(int, input().split())
    villages = [tuple(map(int, input().split())) for _ in range(n)]
    minions = [tuple(map(int, input().split())) for _ in range(m)]
    
    # Calculate the attack radius and area
    radius = get_attack_radius(r, villages)
    area = get_attack_area(center, radius)
    
    # Calculate the number of minions destroyed
    destroyed = get_minions_destroyed(minions, area)
    
    # Print the result
    print(destroyed)

if __name__ == '__main__':
    main()

