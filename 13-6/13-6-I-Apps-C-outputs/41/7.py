
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

def get_new_lawn_widths(lawn_widths, road_widths):
    new_lawn_widths = []
    for i in range(len(lawn_widths)):
        new_lawn_widths.append(lawn_widths[i] - road_widths[i])
    return new_lawn_widths

def get_solution(n, road_widths, lawn_widths):
    total_lawn_width = get_total_lawn_width(lawn_widths)
    new_road_widths = get_new_road_widths(road_widths, lawn_widths)
    new_lawn_widths = get_new_lawn_widths(lawn_widths, road_widths)
    return total_lawn_width, new_road_widths, new_lawn_widths

def main():
    n = int(input())
    road_widths = []
    lawn_widths = []
    for i in range(n):
        s, g = map(int, input().split())
        road_widths.append(s)
        lawn_widths.append(g)
    total_lawn_width, new_road_widths, new_lawn_widths = get_solution(n, road_widths, lawn_widths)
    print(total_lawn_width)
    for i in range(n):
        print(new_road_widths[i], new_lawn_widths[i])

if __name__ == '__main__':
    main()

