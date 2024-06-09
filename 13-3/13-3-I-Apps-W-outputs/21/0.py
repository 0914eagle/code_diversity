
def get_workpieces(liana, k):
    workpieces = []
    for i in range(0, len(liana), k):
        workpieces.append(liana[i:i+k])
    return workpieces

def get_valid_workpieces(workpieces, schematic):
    valid_workpieces = []
    for workpiece in workpieces:
        if set(workpiece) == set(schematic):
            valid_workpieces.append(workpiece)
    return valid_workpieces

def get_removed_flowers(liana, k, n, schematic):
    workpieces = get_workpieces(liana, k)
    valid_workpieces = get_valid_workpieces(workpieces, schematic)
    if len(valid_workpieces) == 0:
        return -1
    removed_flowers = []
    for i in range(n):
        removed_flowers.append(valid_workpieces[i][:])
    return removed_flowers

def main():
    m, k, n, s = map(int, input().split())
    liana = list(map(int, input().split()))
    schematic = list(map(int, input().split()))
    removed_flowers = get_removed_flowers(liana, k, n, schematic)
    if removed_flowers == -1:
        print(-1)
    else:
        print(len(removed_flowers))
        for removed_flower in removed_flowers:
            print(" ".join(map(str, removed_flower)))

if __name__ == '__main__':
    main()

