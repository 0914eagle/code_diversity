
def get_total_chairs(n, guests):
    total_chairs = 0
    for guest in guests:
        total_chairs += guest[0] + guest[1] + 1
    return total_chairs

def get_min_chairs(n, guests):
    min_chairs = 0
    for guest in guests:
        min_chairs += max(guest[0], guest[1]) + 1
    return min_chairs

def solve(n, guests):
    total_chairs = get_total_chairs(n, guests)
    min_chairs = get_min_chairs(n, guests)
    return max(total_chairs, min_chairs)

if __name__ == '__main__':
    n = int(input())
    guests = []
    for i in range(n):
        l, r = map(int, input().split())
        guests.append([l, r])
    print(solve(n, guests))

