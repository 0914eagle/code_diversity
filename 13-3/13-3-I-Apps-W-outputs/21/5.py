
def f1(m, k, n, s, a, b):
    # Initialize variables
    removed_flowers = 0
    workpieces = []
    current_workpiece = []
    types = []

    # Iterate through the liana
    for i in range(m):
        # If the current flower is not in Diana's schematic, remove it
        if a[i] not in b:
            removed_flowers += 1
        # If the current flower is in Diana's schematic, add it to the current workpiece
        else:
            current_workpiece.append(a[i])
            types.append(a[i])
        # If the current workpiece has k flowers, add it to the list of workpieces
        if len(current_workpiece) == k:
            workpieces.append(current_workpiece)
            current_workpiece = []

    # If there are not enough workpieces, return -1
    if len(workpieces) < n:
        return -1

    # If there are enough workpieces, return the number of removed flowers and the positions of the removed flowers
    return removed_flowers, [i for i in range(m) if a[i] in types]

def f2(...):
    ...

if __name__ == '__main__':
    m, k, n, s, a, b = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*f1(m, k, n, s, a, b))

