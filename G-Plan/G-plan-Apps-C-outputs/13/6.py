
import math

def calculate_chaos(passengers):
    return math.ceil(passengers / 10) * 10

def maximum_chaos(n, passengers, order):
    total_chaos = 0
    max_chaos = 0
    segments = 1

    for coach in order:
        chaos = calculate_chaos(passengers[coach - 1])
        total_chaos += chaos
        max_chaos = max(max_chaos, chaos)

    for i in range(1, n):
        if order[i] < order[i - 1]:
            segments += 1

    return max(total_chaos, max_chaos * segments)

if __name__ == "__main__":
    n = int(input())
    passengers = list(map(int, input().split()))
    order = list(map(int, input().split()))

    result = maximum_chaos(n, passengers, order)
    print(result)