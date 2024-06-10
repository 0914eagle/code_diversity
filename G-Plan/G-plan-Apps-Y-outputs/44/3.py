
import math

def calculate_a(citizens):
    total_x = 0
    total_y = 0
    for x, y in citizens:
        total_x += x
        total_y += y
    avg_x = total_x / len(citizens)
    return -avg_x

if __name__ == "__main__":
    N = int(input())
    citizens = []
    for _ in range(N):
        x, y = map(int, input().split())
        citizens.append((x, y))

    a = calculate_a(citizens)
    print("{:.6f}".format(a))
