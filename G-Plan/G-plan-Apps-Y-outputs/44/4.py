
import math

def calculate_a(coordinates):
    sum_x = sum(coord[0] for coord in coordinates)
    sum_y = sum(coord[1] for coord in coordinates)
    avg_x = sum_x / len(coordinates)
    avg_y = sum_y / len(coordinates)
    return -avg_x

if __name__ == "__main__":
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    a = calculate_a(coordinates)
    print("{:.6f}".format(a))
