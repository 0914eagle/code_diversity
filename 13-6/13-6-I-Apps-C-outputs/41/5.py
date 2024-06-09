
def get_lawn_widths(street_parts):
    total_lawn_width = 0
    new_road_widths = []
    for part in street_parts:
        road_width, lawn_width = part
        new_lawn_width = lawn_width // 2
        total_lawn_width += new_lawn_width
        new_road_widths.append(road_width + new_lawn_width)
    return total_lawn_width, new_road_widths

def solve(street_parts):
    total_lawn_width, new_road_widths = get_lawn_widths(street_parts)
    if total_lawn_width % 2 == 1:
        return -1
    else:
        return total_lawn_width // 2, new_road_widths

if __name__ == '__main__':
    n = int(input())
    street_parts = []
    for _ in range(n):
        street_parts.append(list(map(int, input().split())))
    total_lawn_width, new_road_widths = solve(street_parts)
    print(total_lawn_width)
    print(*new_road_widths)

