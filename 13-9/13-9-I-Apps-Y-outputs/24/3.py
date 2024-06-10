
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def get_max_diff(a):
    max_diff = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            diff = abs(a[i] - a[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def solve():
    n, a = get_input()
    max_diff = get_max_diff(a)
    print(max_diff)

if __name__ == '__main__':
    solve()

