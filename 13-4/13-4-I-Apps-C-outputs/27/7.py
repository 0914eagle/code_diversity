
import sys
import math

def get_input():
    N = int(input())
    customers = []
    for i in range(N):
        x, y = map(int, input().split())
        customers.append((x, y))
    return N, customers

def f1(N, customers):
    # Your code here
    pass

def f2(N, customers):
    # Your code here
    pass

if __name__ == '__main__':
    N, customers = get_input()
    print(max(f1(N, customers), f2(N, customers)))

