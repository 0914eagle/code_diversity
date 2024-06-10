
def f(a, l, r):
    return sorted(set(a) - set(range(l, r + 1)))

def count_sorted_pairs(a, x):
    count = 0
    for l in range(1, x + 1):
        for r in range(l, x + 1):
            if f(a, l, r) == sorted(f(a, l, r)):
                count += 1
    return count

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_sorted_pairs(a, x))

if __name__ == '__main__':
    main()

