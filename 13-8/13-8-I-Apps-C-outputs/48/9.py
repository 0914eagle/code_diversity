
import math

def get_minimum_velocity(mice, multiplicative_factor):
    # Calculate the minimum velocity necessary for Cartesian Cat to eat all the mice
    minimum_velocity = 0
    for mouse in mice:
        distance = math.sqrt(mouse[0] ** 2 + mouse[1] ** 2)
        time = distance / minimum_velocity
        if time < mouse[2]:
            minimum_velocity = distance / mouse[2]
        else:
            minimum_velocity = distance / time
        minimum_velocity *= multiplicative_factor
    return minimum_velocity

def get_optimal_order(mice):
    # Return the optimal order for eating the mice
    return sorted(mices, key=lambda x: x[2])

def main():
    mice = []
    while True:
        try:
            x, y, s = map(int, input().split())
            mice.append((x, y, s))
        except:
            break
    multiplicative_factor = float(input())
    minimum_velocity = get_minimum_velocity(mice, multiplicative_factor)
    print(minimum_velocity)

if __name__ == '__main__':
    main()

