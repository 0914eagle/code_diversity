
def partition_count(a, l, r):
    def is_beautiful_partition(partition):
        return all(s[0] != "0" for s in partition)
    
    def count_partitions(a, l, r):
        if a == 0:
            return 1
        if a < 0 or l > a or r < a:
            return 0
        return count_partitions(a - 1, l, r) + count_partitions(a - 1, l, r - 1)
    
    return count_partitions(a, l, r)

def main():
    a = int(input())
    l = int(input())
    r = int(input())
    print(partition_count(a, l, r) % 998244353)

if __name__ == '__main__':
    main()

