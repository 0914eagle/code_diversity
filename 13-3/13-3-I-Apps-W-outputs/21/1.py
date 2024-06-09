
def get_workpieces(liana, k):
    workpieces = []
    for i in range(0, len(liana), k):
        workpieces.append(liana[i:i+k])
    return workpieces

def get_removed_flowers(liana, k, s, b):
    removed_flowers = []
    for i in range(len(liana)):
        if liana[i] in b:
            removed_flowers.append(i)
            if len(removed_flowers) == s:
                break
    return removed_flowers

def get_workpieces_after_removal(liana, k, s, b, removed_flowers):
    workpieces = []
    for i in range(len(liana)):
        if i not in removed_flowers:
            workpieces.append(liana[i:i+k])
    return workpieces

def solve(liana, k, n, s, b):
    workpieces = get_workpieces(liana, k)
    if len(workpieces) < n:
        return -1
    removed_flowers = get_removed_flowers(liana, k, s, b)
    workpieces_after_removal = get_workpieces_after_removal(liana, k, s, b, removed_flowers)
    if len(workpieces_after_removal) == 0:
        return -1
    return removed_flowers

if __name__ == '__main__':
    m, k, n, s = map(int, input().split())
    liana = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve(liana, k, n, s, b)
    if result == -1:
        print(-1)
    else:
        print(len(result))
        print(*result)

