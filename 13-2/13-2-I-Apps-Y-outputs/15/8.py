
def is_good_sequence(a):
    return all(a.count(x) == x for x in a)

def solve(a):
    n = len(a)
    for i in range(n):
        if is_good_sequence(a[:i] + a[i+1:]):
            return n - i - 1
    return 0

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

