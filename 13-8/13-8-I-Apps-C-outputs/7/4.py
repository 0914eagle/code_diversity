
def get_discrete_dish_tastiness(n, w, t_i, delta_t_i):
    return (t_i - (n-1)*delta_t_i)

def get_continuous_dish_tastiness(x, w, t_i, delta_t_i):
    return (t_i - x*delta_t_i)

def get_max_tastiness(dishes, w):
    max_tastiness = 0
    for dish in dishes:
        if dish[0] == 'D':
            # Discrete dish
            n = int(w / dish[1])
            tastiness = get_discrete_dish_tastiness(n, w, dish[2], dish[3])
            if tastiness > max_tastiness:
                max_tastiness = tastiness
        else:
            # Continuous dish
            x = w / dish[1]
            tastiness = get_continuous_dish_tastiness(x, w, dish[2], dish[3])
            if tastiness > max_tastiness:
                max_tastiness = tastiness
    return max_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        dishes.append(dish)
    print(get_max_tastiness(dishes, w))

if __name__ == '__main__':
    main()

