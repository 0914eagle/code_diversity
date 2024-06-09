
def get_input():
    n = int(input())
    streets = []
    for i in range(n):
        street = list(map(int, input().split()))
        streets.append(street)
    return n, streets

def get_total_width_of_lawns(streets):
    total_width = 0
    for street in streets:
        total_width += street[1]
    return total_width

def get_new_widths(streets):
    new_widths = []
    for street in streets:
        new_width = street[0] + street[1]
        new_widths.append(new_width)
    return new_widths

def check_condition(new_widths):
    for i in range(len(new_widths) - 1):
        if abs(new_widths[i] - new_widths[i + 1]) > 1:
            return False
    return True

def solve(n, streets):
    total_width = get_total_width_of_lawns(streets)
    new_widths = get_new_widths(streets)
    if check_condition(new_widths):
        return total_width, new_widths
    else:
        return -1, []

if __name__ == '__main__':
    n, streets = get_input()
    total_width, new_widths = solve(n, streets)
    print(total_width)
    print(*new_widths)

