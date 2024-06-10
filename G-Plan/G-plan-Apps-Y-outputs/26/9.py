
def can_partition_array(A):
    total_sum = sum(A)
    if total_sum % 3 != 0:
        return False
    
    target_sum = total_sum // 3
    prefix_sums = [0] * len(A)
    prefix_sums[0] = A[0]
    for i in range(1, len(A)):
        prefix_sums[i] = prefix_sums[i - 1] + A[i]
    
    part_sum = 0
    partitions = 0
    for i in range(len(A)):
        if prefix_sums[i] == partitions * target_sum:
            partitions += 1
        if partitions == 3:
            return True
    
    return False

if __name__ == "__main__":
    A = list(map(int, input().strip().split(',')))
    print(can_partition_array(A))
