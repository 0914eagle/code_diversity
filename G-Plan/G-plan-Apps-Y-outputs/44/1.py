
import math

def calculate_a(coordinates):
    total_x = sum(coord[0] for coord in coordinates)
    total_y = sum(coord[1] for coord in coordinates)
    avg_x = total_x / len(coordinates)
    avg_y = total_y / len(coordinates)
    return -avg_x

if __name__ == "__main__":
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    a = calculate_a(coordinates)
    print("{:.6f}".format(a))
