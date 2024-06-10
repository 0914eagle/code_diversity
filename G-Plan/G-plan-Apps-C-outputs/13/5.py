
import math

def calculate_chaos(passengers):
    return math.ceil(passengers / 10) * 10

def max_chaos_during_robbery(n, passengers, order):
    total_chaos = 0
    max_chaos = 0

    for coach in order:
        chaos = calculate_chaos(passengers[coach - 1])
        total_chaos += chaos
        max_chaos = max(max_chaos, chaos)

    return max_chaos

if __name__ == "__main__":
    n = int(input())
    passengers = list(map(int, input().split()))
    order = list(map(int, input().split()))

    result = max_chaos_during_robbery(n, passengers, order)
    print(result)
