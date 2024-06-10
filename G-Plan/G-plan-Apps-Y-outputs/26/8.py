
def can_partition_array(A):
    total_sum = sum(A)
    if total_sum % 3 != 0:
        return False
    
    target_sum = total_sum // 3
    prefix_sums = [0] * len(A)
    prefix_sums[0] = A[0]
    
    for i in range(1, len(A)):
        prefix_sums[i] = prefix_sums[i - 1] + A[i]
    
    partition_points = []
    for i in range(len(A) - 2):
        if prefix_sums[i] == target_sum:
            partition_points.append(i)
    
    for i in partition_points:
        for j in range(i + 1, len(A) - 1):
            if prefix_sums[j] - prefix_sums[i] == target_sum and prefix_sums[-1] - prefix_sums[j] == target_sum:
                return True
    
    return False

if __name__ == "__main__":
    A = list(map(int, input().strip().split(',')))
    print(can_partition_array(A))
