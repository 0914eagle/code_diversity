
def can_partition_array(A):
    total_sum = sum(A)
    if total_sum % 3 != 0:
        return False

    target_sum = total_sum // 3
    prefix_sums = [0] * len(A)
    prefix_sums[0] = A[0]

    for i in range(1, len(A)):
        prefix_sums[i] = prefix_sums[i - 1] + A[i]

    found_first_partition = False
    found_second_partition = False

    for i in range(len(A) - 2):
        if not found_first_partition:
            if prefix_sums[i] == target_sum:
                found_first_partition = True

        if found_first_partition and not found_second_partition:
            if prefix_sums[i] == 2 * target_sum:
                found_second_partition = True

    return found_first_partition and found_second_partition


if __name__ == "__main__":
    A = list(map(int, input().strip().split(',')))
    print(can_partition_array(A))
