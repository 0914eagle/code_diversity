
def get_lawn_width(s, g):
    return s + g

def get_road_width(s, g):
    return s

def get_total_lawn_width(lawn_widths):
    return sum(lawn_widths)

def get_new_road_widths(road_widths, lawn_widths):
    new_road_widths = []
    for i in range(len(road_widths)):
        new_road_widths.append(road_widths[i] + lawn_widths[i])
    return new_road_widths

def get_new_lawn_widths(lawn_widths, x):
    new_lawn_widths = []
    for i in range(len(lawn_widths)):
        new_lawn_widths.append(lawn_widths[i] - x[i])
    return new_lawn_widths

def get_solution(n, s, g, x):
    lawn_widths = get_lawn_width(s, g)
    road_widths = get_road_width(s, g)
    total_lawn_width = get_total_lawn_width(lawn_widths)
    new_road_widths = get_new_road_widths(road_widths, lawn_widths)
    new_lawn_widths = get_new_lawn_widths(lawn_widths, x)
    return total_lawn_width, new_road_widths, new_lawn_widths

def main():
    n = int(input())
    s = list(map(int, input().split()))
    g = list(map(int, input().split()))
    x = list(map(int, input().split()))
    total_lawn_width, new_road_widths, new_lawn_widths = get_solution(n, s, g, x)
    print(total_lawn_width)
    print(*new_road_widths)
    print(*new_lawn_widths)

if __name__ == '__main__':
    main()

