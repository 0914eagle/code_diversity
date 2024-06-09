
def find_regular_polygon(angle):
    for n in range(3, 998244354):
        if n * (n - 3) % 2 == 0:
            continue
        if (n - 3) * 180 % n == angle:
            return n
    return -1

def solve(angle):
    return find_regular_polygon(angle)

if __name__ == '__main__':
    num_queries = int(input())
    for _ in range(num_queries):
        angle = int(input())
        print(solve(angle))

