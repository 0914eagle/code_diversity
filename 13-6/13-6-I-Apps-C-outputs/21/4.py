
def get_discrete_dish(w, wi, ti, dt):
    return (ti - (w-1)*dt) * w

def get_continuous_dish(w, ti, dt):
    return (ti - w*dt) * w

def get_max_tastiness(dishes, w):
    total_tastiness = 0
    for dish in dishes:
        if dish[0] == 'D':
            total_tastiness += get_discrete_dish(w, dish[1], dish[2], dish[3])
        else:
            total_tastiness += get_continuous_dish(w, dish[1], dish[2])
    return total_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        dishes.append([dish[0], int(dish[1]), int(dish[2]), int(dish[3])])
    print(get_max_tastiness(dishes, w))

if __name__ == '__main__':
    main()

