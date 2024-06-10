
import math

def calculate_a(coordinates):
    sum_x = sum(y for x, y in coordinates)
    sum_y = sum(x for x, y in coordinates)
    n = len(coordinates)
    return -sum_y / n

if __name__ == "__main__":
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    result = calculate_a(coordinates)
    print("{:.6f}".format(result))
