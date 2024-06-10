
def calculate_a(citizens):
    sum_x = sum(x for x, _ in citizens)
    sum_y = sum(y for _, y in citizens)
    avg_x = sum_x / len(citizens)
    return -avg_x

if __name__ == "__main__":
    N = int(input())
    citizens = [tuple(map(int, input().split())) for _ in range(N)]
    a = calculate_a(citizens)
    print("{:.6f}".format(a))
