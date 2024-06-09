
def get_workpieces(flowers, k):
    workpieces = []
    for i in range(0, len(flowers), k):
        workpieces.append(flowers[i:i+k])
    return workpieces

def get_removable_flowers(flowers, k, schematic):
    removable_flowers = []
    for i in range(len(flowers)):
        if flowers[i] not in schematic:
            removable_flowers.append(i)
    return removable_flowers

def get_workpieces_with_schematic(flowers, k, schematic):
    workpieces = get_workpieces(flowers, k)
    workpieces_with_schematic = []
    for workpiece in workpieces:
        if set(workpiece).issubset(set(schematic)):
            workpieces_with_schematic.append(workpiece)
    return workpieces_with_schematic

def solve(flowers, k, n, schematic):
    workpieces = get_workpieces(flowers, k)
    if len(workpieces) < n:
        return -1
    removable_flowers = get_removable_flowers(flowers, k, schematic)
    workpieces_with_schematic = get_workpieces_with_schematic(flowers, k, schematic)
    if not workpieces_with_schematic:
        return -1
    return len(removable_flowers)

if __name__ == '__main__':
    m, k, n, s = map(int, input().split())
    flowers = list(map(int, input().split()))
    schematic = list(map(int, input().split()))
    print(solve(flowers, k, n, schematic))

