
import math

def get_mouse_locations(n):
    mouse_locations = []
    for i in range(n):
        x, y, s = map(int, input().split())
        mouse_locations.append((x, y, s))
    return mouse_locations

def get_min_velocity(mouse_locations, m):
    # Sort the mice by their location
    mouse_locations.sort(key=lambda x: x[0])
    
    # Initialize the minimum velocity
    min_velocity = 0
    
    # Loop through the mice and calculate the minimum velocity necessary to eat them all
    for i in range(len(mouse_locations)):
        x, y, s = mouse_locations[i]
        distance = math.sqrt(x**2 + y**2)
        time = distance / min_velocity
        if time < s:
            min_velocity = distance / s * (1 - m**(s-time))
    
    return min_velocity

def main():
    n = int(input())
    mouse_locations = get_mouse_locations(n)
    m = float(input())
    print(get_min_velocity(mouse_locations, m))

if __name__ == '__main__':
    main()

