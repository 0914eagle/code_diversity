
def get_discrete_dish(weight, tastiness, decay):
    return tastiness - (weight - 1) * decay

def get_continuous_dish(weight, tastiness, decay):
    return tastiness - weight * decay

def get_max_tastiness(dishes, weight):
    max_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            max_tastiness += get_discrete_dish(dish[1], dish[2], dish[3])
        else:
            max_tastiness += get_continuous_dish(dish[1], dish[2], dish[3])
    return max_tastiness

def main():
    dishes, weight = map(int, input().split())
    dishes_info = []
    for _ in range(dishes):
        dish = input().split()
        dishes_info.append((dish[0], int(dish[1]), int(dish[2]), int(dish[3])))
    print(get_max_tastiness(dishes_info, weight))

if __name__ == '__main__':
    main()

