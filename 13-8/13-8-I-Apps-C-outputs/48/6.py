
import math

def get_min_velocity(mice, multiplier):
    # Sort the mice by their ducking time in ascending order
    sorted_mice = sorted(mice, key=lambda x: x[2])

    # Initialize the minimum velocity and the current velocity
    min_velocity = 0
    velocity = 1

    # Loop through the mice and calculate the minimum velocity needed to eat them all
    for mouse in sorted_mice:
        # Calculate the distance between the cat and the mouse
        distance = math.sqrt((mouse[0] - 0) ** 2 + (mouse[1] - 0) ** 2)

        # Calculate the time it takes for the cat to reach the mouse
        time = distance / velocity

        # If the cat reaches the mouse before it ducks underground, eat the mouse and update the velocity
        if time < mouse[2]:
            velocity *= multiplier
        # Otherwise, the cat won't be able to eat the mouse, so update the minimum velocity
        else:
            min_velocity = max(min_velocity, velocity)

    return min_velocity

def main():
    # Read the input data
    num_mice = int(input())
    mice = []
    for i in range(num_mice):
        x, y, s = map(int, input().split())
        mice.append([x, y, s])
    multiplier = float(input())

    # Calculate the minimum velocity needed to eat all the mice
    min_velocity = get_min_velocity(mice, multiplier)

    # Print the result
    print(min_velocity)

if __name__ == '__main__':
    main()

