
def get_workpieces(flowers, k):
    workpieces = []
    for i in range(0, len(flowers), k):
        workpieces.append(flowers[i:i+k])
    return workpieces

def get_schematic_workpieces(flowers, schematic):
    workpieces = []
    for i in range(len(schematic)):
        workpieces.append([flowers[i] for i in range(len(flowers)) if flowers[i] == schematic[i]])
    return workpieces

def get_removed_flowers(flowers, schematic, k):
    removed_flowers = []
    for i in range(len(schematic)):
        if schematic[i] not in flowers:
            return -1
        removed_flowers.append(flowers.index(schematic[i]))
    return removed_flowers

def solve(flowers, k, n, schematic):
    workpieces = get_workpieces(flowers, k)
    schematic_workpieces = get_schematic_workpieces(flowers, schematic)
    removed_flowers = get_removed_flowers(flowers, schematic, k)
    if removed_flowers == -1:
        return -1
    return removed_flowers

if __name__ == '__main__':
    flowers = [int(i) for i in input().split()]
    k = int(input())
    n = int(input())
    schematic = [int(i) for i in input().split()]
    print(solve(flowers, k, n, schematic))

