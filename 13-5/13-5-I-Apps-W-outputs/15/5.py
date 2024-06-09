
def is_regular_polygon(ang):
    for n in range(3, 998244354):
        if n * (n - 3) % 2 == 0:
            continue
        if ang % (180 / n) == 0:
            return n
    return -1

def solve(ang):
    return is_regular_polygon(ang)

if __name__ == '__main__':
    ang = int(input())
    print(solve(ang))

