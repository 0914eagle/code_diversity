
def get_workpieces(a, k):
    workpieces = []
    for i in range(0, len(a), k):
        workpieces.append(a[i:i+k])
    return workpieces

def get_removable_flowers(a, b, k):
    removable_flowers = []
    for i in range(len(a)):
        if a[i] in b:
            removable_flowers.append(i)
    return removable_flowers

def get_valid_workpieces(a, b, k):
    workpieces = get_workpieces(a, k)
    valid_workpieces = []
    for workpiece in workpieces:
        if set(workpiece).issubset(set(b)):
            valid_workpieces.append(workpiece)
    return valid_workpieces

def solve(a, k, n, s, b):
    removable_flowers = get_removable_flowers(a, b, k)
    valid_workpieces = get_valid_workpieces(a, b, k)
    if len(valid_workpieces) >= n:
        return -1
    else:
        return removable_flowers[:n-len(valid_workpieces)]

if __name__ == '__main__':
    m, k, n, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve(a, k, n, s, b)
    if result == -1:
        print(-1)
    else:
        print(len(result))
        print(*result)

