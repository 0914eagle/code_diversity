
def get_input():
    n = int(input())
    streets = []
    for i in range(n):
        street = list(map(int, input().split()))
        streets.append(street)
    return n, streets

def solve(n, streets):
    total_width = 0
    for i in range(n):
        total_width += streets[i][1]
    if total_width % 2 == 1:
        return -1
    total_width //= 2
    widths = [0] * n
    for i in range(n):
        widths[i] = streets[i][0] + streets[i][1]
    for i in range(n):
        if widths[i] % 2 == 1:
            return -1
        widths[i] //= 2
    for i in range(n-1):
        if abs(widths[i] - widths[i+1]) > 1:
            return -1
    return total_width

def main():
    n, streets = get_input()
    print(solve(n, streets))

if __name__ == '__main__':
    main()

