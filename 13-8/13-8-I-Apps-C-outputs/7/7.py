
def read_input():
    d, w = map(int, input().split())
    dishes = []
    for _ in range(d):
        line = input()
        if line[0] == "D":
            wi, ti, dt = map(int, line.split()[1:])
            dishes.append((wi, ti, dt))
        elif line[0] == "C":
            ti, dt = map(int, line.split()[1:])
            dishes.append((None, ti, dt))
    return d, w, dishes

def compute_total_tastiness(dishes, w):
    total_tastiness = 0
    for dish in dishes:
        if dish[0] is None:
            total_tastiness += dish[1] * w
        else:
            total_tastiness += dish[1] - (w // dish[0]) * dish[2]
    return total_tastiness

def get_max_total_tastiness(d, w, dishes):
    max_total_tastiness = 0
    for i in range(1, w + 1):
        total_tastiness = compute_total_tastiness(dishes, i)
        if total_tastiness > max_total_tastiness:
            max_total_tastiness = total_tastiness
    return max_total_tastiness

def main():
    d, w, dishes = read_input()
    max_total_tastiness = get_max_total_tastiness(d, w, dishes)
    print(max_total_tastiness)

if __name__ == '__main__':
    main()

