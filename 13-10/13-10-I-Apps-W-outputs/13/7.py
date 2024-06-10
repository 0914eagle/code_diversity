
import itertools

def get_partitions(n):
    # generate all possible partitions of n
    partitions = []
    for i in range(1, n + 1):
        partitions += [[i]]
        for j in range(1, i):
            partitions += [[j, i - j]]
    return partitions

def is_beautiful_partition(partition, l, r):
    # check if the partition is beautiful
    for i in partition:
        if i < l or i > r:
            return False
    return True

def count_beautiful_partitions(n, l, r):
    # count the number of beautiful partitions of n
    count = 0
    for partition in get_partitions(n):
        if is_beautiful_partition(partition, l, r):
            count += 1
    return count

def main():
    n = int(input())
    l = int(input())
    r = int(input())
    print(count_beautiful_partitions(n, l, r) % 998244353)

if __name__ == '__main__':
    main()

