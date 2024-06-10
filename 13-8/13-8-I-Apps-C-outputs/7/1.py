
def get_discrete_tastiness(weight, initial_tastiness, decay_rate):
    return initial_tastiness - (weight - 1) * decay_rate

def get_continuous_tastiness(weight, initial_tastiness, decay_rate):
    return initial_tastiness - weight * decay_rate

def get_total_tastiness(weights, tastinesses, decay_rates):
    total_tastiness = 0
    for weight, tastiness, decay_rate in zip(weights, tastinesses, decay_rates):
        if weight == 0:
            continue
        if weight == 1:
            total_tastiness += get_discrete_tastiness(weight, tastiness, decay_rate)
        else:
            total_tastiness += get_continuous_tastiness(weight, tastiness, decay_rate)
    return total_tastiness

def get_best_meal(desired_weight, dish_weights, dish_tastinesses, dish_decay_rates):
    max_tastiness = 0
    for dish_combination in itertools.product(*[range(dish_weights[i] + 1) for i in range(len(dish_weights))]):
        meal_weight = sum(dish_combination)
        if meal_weight != desired_weight:
            continue
        meal_tastiness = get_total_tastiness(dish_combination, dish_tastinesses, dish_decay_rates)
        if meal_tastiness > max_tastiness:
            max_tastiness = meal_tastiness
    return max_tastiness

def main():
    desired_weight, num_dishes = map(int, input().split())
    dish_weights = []
    dish_tastinesses = []
    dish_decay_rates = []
    for _ in range(num_dishes):
        dish_type, *dish_info = input().split()
        if dish_type == "D":
            dish_weights.append(int(dish_info[0]))
            dish_tastinesses.append(int(dish_info[1]))
            dish_decay_rates.append(int(dish_info[2]))
        elif dish_type == "C":
            dish_weights.append(0)
            dish_tastinesses.append(int(dish_info[0]))
            dish_decay_rates.append(int(dish_info[1]))
    print(get_best_meal(desired_weight, dish_weights, dish_tastinesses, dish_decay_rates))

if __name__ == '__main__':
    main()

