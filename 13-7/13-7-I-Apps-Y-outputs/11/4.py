
def get_subset(x):
    # Sort the list of points
    x.sort()
    # Initialize the subset with the first point
    subset = [x[0]]
    # Iterate through the remaining points
    for i in range(1, len(x)):
        # If the distance between the current point and the last point in the subset is a power of two, add the current point to the subset
        if x[i] - subset[-1] == 2**(len(subset) - 1):
            subset.append(x[i])
    return subset

def main():
    n = int(input())
    x = list(map(int, input().split()))
    subset = get_subset(x)
    print(len(subset))
    print(*subset)

if __name__ == '__main__':
    main()

