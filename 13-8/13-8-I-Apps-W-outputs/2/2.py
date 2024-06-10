
import math
import sys

def get_input():
    n, k = map(int, input().split())
    logs = list(map(int, input().split()))
    return n, k, logs

def cut_log(log, k):
    if k == 0:
        return log
    
    if log == 1:
        return 1
    
    left = math.ceil(log / 2)
    right = math.floor(log / 2)
    return max(cut_log(left, k - 1), cut_log(right, k - 1))

def solve(n, k, logs):
    return max(cut_log(log, k) for log in logs)

if __name__ == '__main__':
    n, k, logs = get_input()
    print(solve(n, k, logs))

