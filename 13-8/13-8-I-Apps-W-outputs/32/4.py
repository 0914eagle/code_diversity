
def get_comfort(cities):
    # Calculate the comfort for each segment
    comfort = 0
    for i in range(len(cities)):
        for j in range(i, len(cities)):
            comfort += cities[i] ^ cities[j]
    return comfort

def get_best_partition(cities):
    # Initialize the best partition with a single segment containing all cities
    best_partition = [[cities[0]]]
    best_comfort = get_comfort(best_partition[0])

    # Iterate over all possible partitions
    for i in range(1, len(cities)):
        for j in range(i, len(cities)):
            # Check if the current partition is better than the previous best partition
            current_partition = best_partition[:]
            current_partition.append(cities[i:j+1])
            current_comfort = get_comfort(current_partition[0])
            for k in range(1, len(current_partition)):
                current_comfort += get_comfort(current_partition[k])
            if current_comfort > best_comfort:
                best_partition = current_partition
                best_comfort = current_comfort

    return best_partition

def main():
    n = int(input())
    cities = [int(x) for x in input().split()]
    best_partition = get_best_partition(cities)
    print(best_partition)
    print(get_comfort(best_partition[0]))

if __name__ == '__main__':
    main()

