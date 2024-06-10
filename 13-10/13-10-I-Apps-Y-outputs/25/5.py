
import math

def get_optimal_c(n, p, s, v):
    # Find the optimal value of c using binary search
    left = 0
    right = 100
    while left <= right:
        mid = (left + right) // 2
        time_taken = get_time_taken(n, p, s, v, mid)
        if time_taken <= 157079:
            right = mid - 1
        else:
            left = mid + 1
    return left

def get_time_taken(n, p, s, v, c):
    # Calculate the time taken to run the algorithm and distribute the keys
    time_taken_algorithm = s * (1 + 1 / c) / v
    time_taken_travel = n * math.log2(n) ** (c * math.sqrt(2)) / (p * 1000000000)
    return time_taken_algorithm + time_taken_travel

def main():
    n, p, s, v = map(float, input().split())
    c = get_optimal_c(n, p, s, v)
    time_taken = get_time_taken(n, p, s, v, c)
    print(f"{time_taken:.10f} {c:.10f}")

if __name__ == '__main__':
    main()

