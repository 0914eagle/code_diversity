
def read_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def get_min_max(a):
    return min(a), max(a)

def solve(n, k, a):
    min_val, max_val = get_min_max(a)
    count = 0
    while min_val != max_val:
        if min_val == 1:
            a[a.index(min_val)] += 1
            min_val += 1
            count += 1
        else:
            a[a.index(max_val)] -= 1
            max_val -= 1
            count += 1
    return count

def main():
    n, k, a = read_input()
    print(solve(n, k, a))

if __name__ == '__main__':
    main()

