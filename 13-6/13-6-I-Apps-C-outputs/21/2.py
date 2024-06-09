
def get_total_tastiness(dishes, w):
    total_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            total_tastiness += dish[1] * (dish[2] - (w // dish[1]) * dish[3])
        else:
            total_tastiness += dish[1] * (dish[2] - w * dish[3])
    return total_tastiness

def get_max_tastiness(dishes, w):
    max_tastiness = 0
    for i in range(len(dishes)):
        for j in range(i+1, len(dishes)):
            total_tastiness = get_total_tastiness(dishes[i:j+1], w)
            if total_tastiness > max_tastiness:
                max_tastiness = total_tastiness
    return max_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        if dish[0] == "D":
            dishes.append([dish[0], int(dish[1]), int(dish[2]), int(dish[3])])
        else:
            dishes.append([dish[0], int(dish[1]), int(dish[2])])
    print(get_max_tastiness(dishes, w))

if __name__ == '__main__':
    main()

