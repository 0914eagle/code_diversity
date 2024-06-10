
import math

def get_mouse_distance(mouse):
    return math.sqrt(mouse[0]**2 + mouse[1]**2)

def get_velocity(mouse, cat_velocity, m):
    return cat_velocity * m

def get_time_to_eat(mouse, cat_velocity, m):
    return get_mouse_distance(mouse) / get_velocity(mouse, cat_velocity, m)

def get_optimal_velocity(mice, m):
    cat_velocity = 1
    for mouse in mice:
        time_to_eat = get_time_to_eat(mouse, cat_velocity, m)
        if time_to_eat > mouse[2]:
            return None
        cat_velocity = get_velocity(mouse, cat_velocity, m)
    return cat_velocity

def main():
    n = int(input())
    mice = []
    for i in range(n):
        mouse = [int(x) for x in input().split()]
        mice.append(mouse)
    m = float(input())
    optimal_velocity = get_optimal_velocity(mice, m)
    print(optimal_velocity)

if __name__ == '__main__':
    main()

