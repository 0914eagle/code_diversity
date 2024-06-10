
import math

def get_velocity(n, mice, m):
    # Initialize the minimum velocity
    velocity = 0

    # Loop through the mice and calculate the minimum velocity necessary to eat them all
    for mouse in mice:
        # Calculate the distance between the cat and the mouse
        distance = math.sqrt((mouse[0] - 0)**2 + (mouse[1] - 0)**2)

        # Calculate the time it takes for the cat to reach the mouse
        time = distance / velocity

        # Calculate the velocity after eating the mouse
        velocity = velocity * m

        # Calculate the time it takes for the cat to reach the next mouse
        time += distance / velocity

        # Update the minimum velocity
        velocity = max(velocity, mouse[2] / time)

    return velocity

def main():
    n = int(input())
    mice = []
    for i in range(n):
        mouse = list(map(int, input().split()))
        mice.append(mouse)
    m = float(input())
    print(get_velocity(n, mice, m))

if __name__ == '__main__':
    main()

