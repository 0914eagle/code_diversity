
import math

def calculate_chaos(passengers):
    return math.ceil(passengers / 10) * 10

def maximum_chaos(n, passengers, order):
    total_chaos = 0
    max_chaos = 0
    segments = 1

    for i in order:
        chaos = calculate_chaos(passengers[i - 1])
        total_chaos += chaos
        max_chaos = max(max_chaos, chaos)

        if i == n:
            break

        if i == segments:
            segments += 1

    return max_chaos * segments

if __name__ == "__main__":
    n = int(input())
    passengers = list(map(int, input().split()))
    order = list(map(int, input().split()))

    result = maximum_chaos(n, passengers, order)
    print(result)
