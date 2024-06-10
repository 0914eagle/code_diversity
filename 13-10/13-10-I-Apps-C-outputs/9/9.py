
import sys
import itertools

def get_input():
    l1, l2, n = map(int, input().split())
    tubes = [int(input()) for _ in range(n)]
    return l1, l2, tubes

def get_max_length(l1, l2, tubes):
    pairs = list(itertools.combinations(tubes, 2))
    max_length = 0
    for pair in pairs:
        if sum(pair) <= l1 and sum(pair) + l2 <= l2:
            max_length = max(max_length, sum(pair))
    return max_length

def main():
    l1, l2, tubes = get_input()
    print(get_max_length(l1, l2, tubes))

if __name__ == '__main__':
    main()

