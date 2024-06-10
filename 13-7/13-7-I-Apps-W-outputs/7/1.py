
def is_regular_polygon(a):
    return a % 180 == 0 or a % 90 == 0

def solve(a):
    if is_regular_polygon(a):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = int(input())
        print(solve(a))

