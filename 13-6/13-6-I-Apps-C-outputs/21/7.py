
def get_discrete_tastiness(n, wi, ti, dt):
    return ti - (n-1)*dt

def get_continuous_tastiness(x, wi, ti, dt):
    return ti - x*dt

def get_max_tastiness(dishes, w):
    max_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            n = int(w/dish[1])
            tastiness = get_discrete_tastiness(n, dish[1], dish[2], dish[3])
            max_tastiness += tastiness
        else:
            x = w*dish[2]
            tastiness = get_continuous_tastiness(x, dish[1], dish[2], dish[3])
            max_tastiness += tastiness
    return max_tastiness

def main():
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        dishes.append(dish)
    print(get_max_tastiness(dishes, w))

if __name__ == '__main__':
    main()

