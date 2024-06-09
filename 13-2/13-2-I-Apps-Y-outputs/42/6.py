
import sys

def solve():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            total += int(x)
        elif u == "BTC":
            total += float(x) * 380000.0
    return total

if __name__ == "__main__":
    print(solve())

