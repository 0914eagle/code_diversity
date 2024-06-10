
import math

def discrete_dish(weight, tastiness, decay):
    return tastiness - decay * (weight - 1)

def continuous_dish(weight, tastiness, decay):
    return tastiness - decay * weight

def get_max_tastiness(dishes, weight):
    max_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            max_tastiness += discrete_dish(dish[1], dish[2], dish[3])
        else:
            max_tastiness += continuous_dish(dish[1], dish[2], dish[3])
    return max_tastiness

def main():
    dishes, weight = [int(x) for x in input().split()]
    dishes = [input().split() for _ in range(dishes)]
    max_tastiness = get_max_tastiness(dishes, weight)
    print(f"{max_tastiness:.6f}")

if __name__ == '__main__':
    main()

