
def f1(m, k, n, s, a, b):
    # Initialize variables
    total_flowers = m
    removed_flowers = 0
    workpieces = []
    schematic = []

    # Convert input lists to arrays
    a = np.array(a)
    b = np.array(b)

    # Sort the liana by type
    a = np.sort(a)

    # Create a schematic for the wreath
    for i in range(s):
        schematic.append(b[i])

    # Remove flowers from the liana
    while total_flowers >= k:
        # Check if the current workpiece fits the schematic
        if np.array_equal(a[:k], schematic):
            workpieces.append(a[:k])
            a = a[k:]
            total_flowers -= k
            removed_flowers += k
        else:
            a = a[1:]
            total_flowers -= 1
            removed_flowers += 1

    # Check if there are enough workpieces to fulfill the requirements
    if len(workpieces) < n:
        return -1
    else:
        return removed_flowers

def f2(m, k, n, s, a, b):
    # Initialize variables
    total_flowers = m
    removed_flowers = 0
    workpieces = []
    schematic = []

    # Convert input lists to arrays
    a = np.array(a)
    b = np.array(b)

    # Sort the liana by type
    a = np.sort(a)

    # Create a schematic for the wreath
    for i in range(s):
        schematic.append(b[i])

    # Remove flowers from the liana
    while total_flowers >= k:
        # Check if the current workpiece fits the schematic
        if np.array_equal(a[:k], schematic):
            workpieces.append(a[:k])
            a = a[k:]
            total_flowers -= k
            removed_flowers += k
        else:
            a = a[1:]
            total_flowers -= 1
            removed_flowers += 1

    # Check if there are enough workpieces to fulfill the requirements
    if len(workpieces) < n:
        return -1
    else:
        return removed_flowers

if __name__ == '__main__':
    m = 13
    k = 4
    n = 3
    s = 3
    a = [3, 2, 6, 4, 1, 4, 4, 7, 1, 3, 3, 2, 4]
    b = [4, 3, 4]
    print(f1(m, k, n, s, a, b))
    print(f2(m, k, n, s, a, b))

