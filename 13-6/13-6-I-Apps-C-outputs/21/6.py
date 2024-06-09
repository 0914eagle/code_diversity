
def get_discrete_dish_tastiness(weight, tastiness, decay):
    return tastiness - (weight - 1) * decay

def get_continuous_dish_tastiness(weight, tastiness, decay):
    return tastiness - weight * decay

def get_meal_tastiness(dishes, weights):
    total_tastiness = 0
    for dish, weight in zip(dishes, weights):
        if dish[0] == "D":
            total_tastiness += get_discrete_dish_tastiness(weight, dish[1], dish[2])
        else:
            total_tastiness += get_continuous_dish_tastiness(weight, dish[1], dish[2])
    return total_tastiness

def get_optimal_weights(dishes, total_weight):
    # Initialize the weights to zero
    weights = [0] * len(dishes)
    # Loop through each dish and try to find the maximum weight that can be taken
    for i in range(len(dishes)):
        dish = dishes[i]
        if dish[0] == "D":
            # Discrete dish, try to take the maximum number of items
            max_weight = dish[1]
            while max_weight <= total_weight:
                weights[i] += 1
                total_weight -= max_weight
        else:
            # Continuous dish, try to take the maximum amount
            max_weight = total_weight
            weights[i] += max_weight
            total_weight -= max_weight
    return weights

def get_optimal_meal_tastiness(dishes, total_weight):
    weights = get_optimal_weights(dishes, total_weight)
    return get_meal_tastiness(dishes, weights)

def main():
    dishes, total_weight = read_input()
    print(get_optimal_meal_tastiness(dishes, total_weight))

def read_input():
    dishes = []
    total_weight = int(input())
    for _ in range(total_weight):
        dish = input().split()
        if dish[0] == "D":
            dish = [dish[0], int(dish[1]), int(dish[2]), int(dish[3])]
        else:
            dish = [dish[0], int(dish[1]), int(dish[2])]
        dishes.append(dish)
    return dishes, total_weight

if __name__ == '__main__':
    main()

