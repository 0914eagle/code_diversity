
def calculate_a(N, homes):
    sum_x = sum(x for x, _ in homes)
    sum_y = sum(y for _, y in homes)
    a = -sum_x / N
    return a

if __name__ == "__main__":
    N = int(input())
    homes = [tuple(map(int, input().split())) for _ in range(N)]
    result = calculate_a(N, homes)
    print("{:.6f}".format(result))
