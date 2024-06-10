
import math

def compute_optimal_tour_length(n, s):
    return s * (1 + 1 / c)

def compute_time_to_distribute_keys(n, p, s, v, c):
    optimal_tour_length = compute_optimal_tour_length(n, s)
    return optimal_tour_length / v

def find_optimal_c(n, p, s, v):
    low = 0
    high = 100
    while low <= high:
        mid = (low + high) // 2
        time_to_distribute_keys = compute_time_to_distribute_keys(n, p, s, v, mid)
        if time_to_distribute_keys <= 157079:
            high = mid - 1
        else:
            low = mid + 1
    return mid

def main():
    n, p, s, v = map(float, input().split())
    c = find_optimal_c(n, p, s, v)
    time_to_distribute_keys = compute_time_to_distribute_keys(n, p, s, v, c)
    print(time_to_distribute_keys, c)

if __name__ == '__main__':
    main()

