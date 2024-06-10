
import sys

def read_input():
    n, *colors = map(int, input().split())
    k = int(input())
    c = set(map(int, input().split()))
    l = int(input())
    s = set(map(int, input().split()))
    return n, colors, k, c, l, s

def get_combinations(colors, k, c, l, s):
    combinations = 0
    for i in range(len(colors)):
        if colors[i] in c:
            continue
        combinations += get_combinations(colors[i+1:], k-1, c-{colors[i]}, l, s)
    if not k:
        return 1
    return combinations

def get_arrangements(n, colors, k, c, l, s):
    arrangements = 0
    for i in range(n):
        if colors[i] in c:
            continue
        arrangements += get_combinations(colors[i+1:], k-1, c-{colors[i]}, l, s)
    return arrangements

def main():
    n, colors, k, c, l, s = read_input()
    arrangements = get_arrangements(n, colors, k, c, l, s)
    print(arrangements % 1000000007)

if __name__ == '__main__':
    main()

