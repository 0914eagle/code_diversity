
def get_discrete_dish_tastiness(num_items, initial_tastiness, decay_rate):
    return initial_tastiness - (num_items - 1) * decay_rate

def get_continuous_dish_tastiness(total_weight, initial_tastiness, decay_rate):
    return initial_tastiness - total_weight * decay_rate

def get_max_meal_tastiness(dishes, total_weight):
    max_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            num_items = total_weight // dish[1]
            tastiness = get_discrete_dish_tastiness(num_items, dish[2], dish[3])
            max_tastiness += tastiness
        else:
            tastiness = get_continuous_dish_tastiness(total_weight, dish[1], dish[2])
            max_tastiness += tastiness
    return max_tastiness

def main():
    dishes = []
    total_weight = int(input())
    for _ in range(int(input())):
        dish = input().split()
        if dish[0] == "D":
            dishes.append(tuple(map(int, dish[1:])))
        else:
            dishes.append(tuple(map(int, dish[1:])))
    print(get_max_meal_tastiness(dishes, total_weight))

if __name__ == '__main__':
    main()

