
import math
import sys

def get_input():
    n, k = map(int, input().split())
    logs = list(map(int, input().split()))
    return n, k, logs

def get_max_length(logs, k):
    max_length = 0
    for log in logs:
        max_length = max(max_length, log)
    return max_length

def get_optimal_length(logs, k):
    max_length = get_max_length(logs, k)
    optimal_length = max_length
    for i in range(k):
        new_logs = []
        for log in logs:
            if log == max_length:
                break
            new_logs.append(math.ceil(log / 2))
        max_length = get_max_length(new_logs, k - i - 1)
        optimal_length = min(optimal_length, max_length)
    return optimal_length

def main():
    n, k, logs = get_input()
    print(get_optimal_length(logs, k))

if __name__ == '__main__':
    main()

