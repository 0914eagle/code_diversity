
def get_discrete_dish_tastiness(n, w, t, dt):
    return t - (n-1)*dt

def get_continuous_dish_tastiness(x, w, t, dt):
    return (t - x*dt)*x

def get_max_tastiness(dishes, w):
    max_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            n = w//dish[1]
            tastiness = get_discrete_dish_tastiness(n, dish[1], dish[2], dish[3])
        else:
            x = w*dish[2]
            tastiness = get_continuous_dish_tastiness(x, dish[1], dish[2], dish[3])
        max_tastiness += tastiness
    return max_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for _ in range(d):
        dish = input().split()
        if dish[0] == "D":
            dish = (dish[0], int(dish[1]), int(dish[2]), int(dish[3]))
        else:
            dish = (dish[0], int(dish[1]), int(dish[2]), int(dish[3]))
        dishes.append(dish)
    print(get_max_tastiness(dishes, w))

if __name__ == '__main__':
    main()

