
def get_workpieces(m, k, n, s, a, b):
    # Initialize variables
    workpieces = []
    removed_flowers = 0
    current_workpiece = []
    current_flower_types = []

    # Iterate through the liana
    for i in range(m):
        # If the current flower type is in Diana's schematic, add it to the current workpiece
        if a[i] in b:
            current_workpiece.append(a[i])
            current_flower_types.append(a[i])

        # If the current workpiece has k flowers, add it to the list of workpieces
        if len(current_workpiece) == k:
            workpieces.append(current_workpiece)
            current_workpiece = []
            current_flower_types = []

        # If the current workpiece has less than k flowers and the liana has less than k flowers left, add the remaining flowers to the workpiece
        if len(current_workpiece) < k and m - i < k:
            current_workpiece.extend(a[i:])
            workpieces.append(current_workpiece)
            break

    # If there are not enough workpieces, return -1
    if len(workpieces) < n:
        return -1

    # If there are enough workpieces, return the number of removed flowers and the positions of the removed flowers
    removed_flowers = m - k * len(workpieces)
    removed_positions = [i for i in range(1, m + 1) if a[i - 1] in current_flower_types]
    return removed_flowers, removed_positions

def main():
    m, k, n, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    removed_flowers, removed_positions = get_workpieces(m, k, n, s, a, b)
    if removed_flowers == -1:
        print(-1)
    else:
        print(removed_flowers)
        print(*removed_positions)

if __name__ == '__main__':
    main()

