
import math

def calculate_velocity(distance, time):
    return distance / time

def calculate_minimum_velocity(mice, multiplier):
    velocities = []
    for mouse in mice:
        velocity = calculate_velocity(mouse[0], mouse[1])
        velocities.append(velocity)
        velocities.append(velocity * multiplier)
    return min(velocities)

def main():
    mice = []
    num_mice = int(input())
    for i in range(num_mice):
        mouse = [int(x) for x in input().split()]
        mice.append(mouse)
    multiplier = float(input())
    minimum_velocity = calculate_minimum_velocity(mice, multiplier)
    print(minimum_velocity)

if __name__ == '__main__':
    main()

