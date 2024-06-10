
def get_total_tastiness(dishes, w):
    total_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            total_tastiness += dish[1] * (dish[2] - (w // dish[1]) * dish[3])
        elif dish[0] == "C":
            total_tastiness += (dish[1] - w * dish[2]) * w
    return total_tastiness

def get_max_tastiness(dishes, w):
    max_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            for i in range(1, w // dish[1] + 1):
                tastiness = dish[1] * (dish[2] - (i - 1) * dish[3])
                if tastiness > max_tastiness:
                    max_tastiness = tastiness
        elif dish[0] == "C":
            tastiness = (dish[1] - w * dish[2]) * w
            if tastiness > max_tastiness:
                max_tastiness = tastiness
    return max_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        dishes.append([dish[0], int(dish[1]), int(dish[2]), int(dish[3])])
    print(get_max_tastiness(dishes, w))

if __name__ == '__main__':
    main()

