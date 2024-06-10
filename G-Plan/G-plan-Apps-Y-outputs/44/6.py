
import math

def calculate_a(citizens):
    sum_x = 0
    sum_y = 0
    for x, y in citizens:
        sum_x += x
        sum_y += y
    avg_x = sum_x / len(citizens)
    avg_y = sum_y / len(citizens)
    return -avg_x

if __name__ == "__main__":
    N = int(input())
    citizens = []
    for _ in range(N):
        x, y = map(int, input().split())
        citizens.append((x, y))
    
    result = calculate_a(citizens)
    print("{:.6f}".format(result))
