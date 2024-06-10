
def get_discrete_dishes(dishes):
    discrete_dishes = []
    for dish in dishes:
        if dish[0] == "D":
            discrete_dishes.append(dish)
    return discrete_dishes

def get_continuous_dishes(dishes):
    continuous_dishes = []
    for dish in dishes:
        if dish[0] == "C":
            continuous_dishes.append(dish)
    return continuous_dishes

def get_total_tastiness(dishes, weight):
    total_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            num_items = weight // dish[1]
            total_tastiness += num_items * (dish[2] - (num_items - 1) * dish[3])
        elif dish[0] == "C":
            total_tastiness += dish[2] - weight * dish[3]
    return total_tastiness

def get_max_total_tastiness(dishes, weight):
    discrete_dishes = get_discrete_dishes(dishes)
    continuous_dishes = get_continuous_dishes(dishes)
    max_total_tastiness = 0
    for i in range(len(discrete_dishes) + 1):
        for j in range(len(continuous_dishes) + 1):
            total_weight = sum([dish[1] for dish in discrete_dishes[0:i]]) + sum([dish[2] for dish in continuous_dishes[0:j]])
            if total_weight == weight:
                total_tastiness = get_total_tastiness(discrete_dishes[0:i] + continuous_dishes[0:j], weight)
                max_total_tastiness = max(max_total_tastiness, total_tastiness)
    return max_total_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        dishes.append(dish)
    print(get_max_total_tastiness(dishes, w))

if __name__ == '__main__':
    main()

