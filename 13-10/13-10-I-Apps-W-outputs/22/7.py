
def f(arr, l, r):
    return [x for x in arr if x < l or x > r]

def solve(arr, x):
    count = 0
    for l in range(1, x+1):
        for r in range(l, x+1):
            if sorted(f(arr, l, r)) == f(arr, l, r):
                count += 1
    return count

if __name__ == '__main__':
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, x))

