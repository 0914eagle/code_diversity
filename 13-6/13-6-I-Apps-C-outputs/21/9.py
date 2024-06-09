
def get_discrete_dish_tastiness(n, w, t, dt):
    return t - (n-1)*dt

def get_continuous_dish_tastiness(x, w, t, dt):
    return (t - x*dt)*x

def get_total_tastiness(dishes, w):
    total_tastiness = 0
    for dish in dishes:
        if dish[0] == "D":
            n = int(w/dish[1])
            total_tastiness += get_discrete_dish_tastiness(n, dish[1], dish[2], dish[3])
        else:
            total_tastiness += get_continuous_dish_tastiness(w, dish[1], dish[2], dish[3])
    return total_tastiness

def solve(d, w, dishes):
    max_tastiness = 0
    for i in range(1, w+1):
        total_tastiness = get_total_tastiness(dishes, i)
        if total_tastiness > max_tastiness:
            max_tastiness = total_tastiness
    return max_tastiness

if __name__ == '__main__':
    d, w = map(int, input().split())
    dishes = []
    for i in range(d):
        dish = input().split()
        if dish[0] == "D":
            dishes.append(tuple(map(int, dish)))
        else:
            dishes.append(tuple(map(int, dish[1:])))
    print(solve(d, w, dishes))

