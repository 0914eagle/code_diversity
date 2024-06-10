
def get_min_operations(a):
    n = len(a)
    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
    return count

def rearrange_marbles(a):
    n = len(a)
    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
            a[i], a[i+1] = a[i+1], a[i]
    return count

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(rearrange_marbles(a))

