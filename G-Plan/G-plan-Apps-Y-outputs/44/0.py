
import sys

def calculate_optimal_a(N, citizens):
    sum_x = sum(x for x, _ in citizens)
    sum_y = sum(y for _, y in citizens)
    return -sum_x / N

if __name__ == "__main__":
    N = int(input())
    citizens = [tuple(map(int, input().split())) for _ in range(N)]
    optimal_a = calculate_optimal_a(N, citizens)
    print("{:.6f}".format(optimal_a))
