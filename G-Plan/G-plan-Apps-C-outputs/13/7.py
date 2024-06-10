
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
        
        if coach == n:
            break
        segments = max(segments, coach)

    return max(total_chaos, segments * total_chaos)

if __name__ == "__main__":
    n = int(input())
    passengers = list(map(int, input().split()))
    order = list(map(int, input().split()))
    
    result = maximum_chaos(n, passengers, order)
    print(result)
