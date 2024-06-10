
def get_max_subset(n, x):
    # Sort the array
    x.sort()
    
    # Initialize variables
    max_subset = []
    current_subset = []
    current_subset_size = 0
    
    # Iterate through the array
    for i in range(n):
        # If the current element is a power of 2, add it to the current subset
        if x[i] == 2**current_subset_size:
            current_subset.append(x[i])
            current_subset_size += 1
        # If the current element is not a power of 2, check if it is a power of 2 plus the last element of the current subset
        elif x[i] == 2**current_subset_size + current_subset[-1]:
            current_subset.append(x[i])
            current_subset_size += 1
        # If the current element is not a power of 2 and is not equal to the last element of the current subset plus 1, start a new subset
        else:
            if current_subset_size > len(max_subset):
                max_subset = current_subset[:]
            current_subset = [x[i]]
            current_subset_size = 1
    
    # Add the last subset to the maximum subset if it is larger than the current maximum subset
    if current_subset_size > len(max_subset):
        max_subset = current_subset[:]
    
    return max_subset

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(len(get_max_subset(n, x)))
    print(" ".join(str(x) for x in get_max_subset(n, x)))

if __name__ == '__main__':
    main()

