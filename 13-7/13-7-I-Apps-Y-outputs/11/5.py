
def get_subset(x):
    # Sort the input array
    x.sort()
    # Initialize the subset with the first element
    subset = [x[0]]
    # Iterate over the remaining elements
    for i in range(1, len(x)):
        # If the current element is a power of two away from the last element in the subset, add it to the subset
        if x[i] - subset[-1] == 2**(len(subset)-1):
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

