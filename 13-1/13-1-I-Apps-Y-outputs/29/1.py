
def is_good_sequence(a):
    return all(a.count(x) == x for x in a)

def solve(a):
    n = len(a)
    if n == 0:
        return 0
    if is_good_sequence(a):
        return 0
    for i in range(n):
        a_copy = a[:i] + a[i+1:]
        if is_good_sequence(a_copy):
            return 1
    return n

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))
