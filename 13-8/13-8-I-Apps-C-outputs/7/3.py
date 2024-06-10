
import math

def get_total_tastiness(dishes, w):
    total_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            total_tastiness += get_discrete_tastiness(dish[1], dish[2], dish[3], w)
        else:
            total_tastiness += get_continuous_tastiness(dish[1], dish[2], dish[3], w)
    return total_tastiness

def get_discrete_tastiness(w, t, dt, w_total):
    n = w_total // w
    return t - (n-1)*dt

def get_continuous_tastiness(t, dt, w_total):
    return t - w_total*dt

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        dishes.append(dish)
    print(get_total_tastiness(dishes, w))

if __name__ == '__main__':
    main()

