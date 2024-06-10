
import sys

def get_input():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        yield n, a

def solve(n, a):
    # Your code here
    pass

def main():
    for n, a in get_input():
        result = solve(n, a)
        if result:
            print("YES")
            for road in result:
                print(" ".join(map(str, road)))
        else:
            print("NO")

if __name__ == '__main__':
    main()

