
def get_subset_with_max_distance_power_of_two(n, x):
    # Sort the input array
    x.sort()
    
    # Initialize variables
    max_subset_size = 0
    current_subset_size = 0
    current_subset = []
    
    # Iterate over the input array
    for i in range(n):
        # If the current element is a power of two, add it to the current subset
        if x[i] == 2**current_subset_size:
            current_subset.append(x[i])
            current_subset_size += 1
        # If the current element is not a power of two, check if it is a power of two plus the previous element
        elif x[i] == 2**current_subset_size + current_subset[-1]:
            current_subset.append(x[i])
            current_subset_size += 1
        # If the current element is neither a power of two nor a power of two plus the previous element, start a new subset
        else:
            if current_subset_size > max_subset_size:
                max_subset_size = current_subset_size
            current_subset = [x[i]]
            current_subset_size = 1
    
    # If the last subset has more elements than the current maximum, update the maximum
    if current_subset_size > max_subset_size:
        max_subset_size = current_subset_size
    
    return max_subset_size, current_subset

def main():
    n = int(input())
    x = list(map(int, input().split()))
    max_subset_size, max_subset = get_subset_with_max_distance_power_of_two(n, x)
    print(max_subset_size)
    print(*max_subset)

if __name__ == '__main__':
    main()

