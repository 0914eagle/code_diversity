
import math

def calculate_a(coordinates):
    sum_x = sum(x for x, _ in coordinates)
    sum_y = sum(y for _, y in coordinates)
    avg_x = sum_x / len(coordinates)
    return -avg_x

if __name__ == "__main__":
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    
    a = calculate_a(coordinates)
    print("{:.6f}".format(a))
