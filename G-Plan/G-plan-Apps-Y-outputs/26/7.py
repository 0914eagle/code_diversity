
def can_partition_array(A):
    prefix_sums = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        prefix_sums[i] = prefix_sums[i - 1] + A[i - 1]
    
    total_sum = prefix_sums[-1]
    
    if total_sum % 3 != 0:
        return False
    
    target_sum = total_sum // 3
    count = 0
    partition_sums = [0, 0, 0]
    
    for i in range(1, len(A)):
        if partition_sums[0] != target_sum:
            partition_sums[0] = prefix_sums[i]
        if partition_sums[1] != target_sum:
            partition_sums[1] = prefix_sums[i + 1]
        if partition_sums[2] != target_sum:
            partition_sums[2] = total_sum
        
        if partition_sums[0] == partition_sums[1] == partition_sums[2]:
            count += 1
            if count == 2:
                return True
    
    return False

if __name__ == "__main__":
    A = list(map(int, input().strip().split(',')))
    print(can_partition_array(A))
