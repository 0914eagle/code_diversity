
import sys

def get_partitions(a):
    partitions = []
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            for k in range(1, a + 1):
                if i + j + k == a:
                    partitions.append([i, j, k])
    return partitions

def is_beautiful_partition(partition, l, r):
    for i in partition:
        if i < l or i > r:
            return False
    return True

def count_beautiful_partitions(a, l, r):
    partitions = get_partitions(a)
    count = 0
    for partition in partitions:
        if is_beautiful_partition(partition, l, r):
            count += 1
    return count

def main():
    a = int(input())
    l = int(input())
    r = int(input())
    result = count_beautiful_partitions(a, l, r)
    print(result % 998244353)

if __name__ == '__main__':
    main()

