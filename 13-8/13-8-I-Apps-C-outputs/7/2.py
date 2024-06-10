
def get_discrete_dish_tastiness(dish_weight, initial_tastiness, decay_rate):
    return initial_tastiness - (dish_weight - 1) * decay_rate

def get_continuous_dish_tastiness(dish_weight, initial_tastiness, decay_rate, current_weight):
    return (initial_tastiness - current_weight * decay_rate) * dish_weight

def get_max_tastiness(dishes, desired_weight):
    max_tastiness = 0
    current_weight = 0
    for dish in dishes:
        if dish[0] == "D":
            dish_weight = dish[1]
            initial_tastiness = dish[2]
            decay_rate = dish[3]
            dish_tastiness = get_discrete_dish_tastiness(dish_weight, initial_tastiness, decay_rate)
            if current_weight + dish_weight <= desired_weight:
                max_tastiness += dish_tastiness
                current_weight += dish_weight
            else:
                max_tastiness += dish_tastiness * (desired_weight - current_weight + 1) / dish_weight
                break
        else:
            dish_weight = 1
            initial_tastiness = dish[1]
            decay_rate = dish[2]
            dish_tastiness = get_continuous_dish_tastiness(dish_weight, initial_tastiness, decay_rate, current_weight)
            max_tastiness += dish_tastiness * (desired_weight - current_weight)
            current_weight = desired_weight
    return max_tastiness

def main():
    dishes, desired_weight = input().split()
    dishes = [input().split() for _ in range(int(dishes))]
    print(get_max_tastiness(dishes, int(desired_weight)))

if __name__ == '__main__':
    main()

