
def get_discrete_dish_tastiness(weight, initial_tastiness, decay_rate):
    return initial_tastiness - (weight - 1) * decay_rate

def get_continuous_dish_tastiness(weight, initial_tastiness, decay_rate):
    return initial_tastiness - weight * decay_rate

def get_meal_tastiness(dishes, weight):
    meal_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            meal_tastiness += get_discrete_dish_tastiness(dish[1], dish[2], dish[3])
        else:
            meal_tastiness += get_continuous_dish_tastiness(dish[1], dish[2], dish[3])
    return meal_tastiness

def get_max_meal_tastiness(dishes, weight):
    max_tastiness = 0
    for i in range(len(dishes)):
        dish = dishes[i]
        if dish[0] == "D":
            for j in range(1, dish[1] + 1):
                tastiness = get_discrete_dish_tastiness(j, dish[2], dish[3])
                if tastiness > max_tastiness:
                    max_tastiness = tastiness
        else:
            for j in range(1, 10001):
                tastiness = get_continuous_dish_tastiness(j, dish[1], dish[2])
                if tastiness > max_tastiness:
                    max_tastiness = tastiness
    return max_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        dishes.append(dish)
    max_tastiness = get_max_meal_tastiness(dishes, w)
    print(max_tastiness)

if __name__ == '__main__':
    main()

