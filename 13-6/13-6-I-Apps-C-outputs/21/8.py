
def f1(d, w):
    # Initialize variables
    total_tastiness = 0
    discrete_dishes = []
    continuous_dishes = []

    # Read input
    for i in range(d):
        line = input()
        if line[0] == "D":
            discrete_dishes.append(line.split())
        else:
            continuous_dishes.append(line.split())

    # Calculate total tastiness for discrete dishes
    for dish in discrete_dishes:
        weight = int(dish[1])
        tastiness = int(dish[2])
        decay = int(dish[3])
        num_items = int(w / weight)
        total_tastiness += num_items * (tastiness - (num_items - 1) * decay)

    # Calculate total tastiness for continuous dishes
    for dish in continuous_dishes:
        tastiness = int(dish[1])
        decay = int(dish[2])
        total_tastiness += (tastiness - w * decay) * w

    return total_tastiness

def f2(d, w):
    # Initialize variables
    total_tastiness = 0
    discrete_dishes = []
    continuous_dishes = []

    # Read input
    for i in range(d):
        line = input()
        if line[0] == "D":
            discrete_dishes.append(line.split())
        else:
            continuous_dishes.append(line.split())

    # Calculate total tastiness for discrete dishes
    for dish in discrete_dishes:
        weight = int(dish[1])
        tastiness = int(dish[2])
        decay = int(dish[3])
        num_items = int(w / weight)
        total_tastiness += num_items * (tastiness - (num_items - 1) * decay)

    # Calculate total tastiness for continuous dishes
    for dish in continuous_dishes:
        tastiness = int(dish[1])
        decay = int(dish[2])
        total_tastiness += (tastiness - w * decay) * w

    return total_tastiness

if __name__ == '__main__':
    d, w = map(int, input().split())
    print(f1(d, w))

