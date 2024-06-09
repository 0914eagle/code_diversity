
def solve(n, permutation):
    # Calculate the number of inversions in the original permutation
    inversions = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                inversions += 1

    # Calculate the expected number of inversions after one operation
    expected_inversions = 0
    for l in range(n):
        for r in range(l, n):
            k = r - l + 1
            for p in range(1, k + 1):
                # Calculate the number of inversions in the transformed permutation
                transformed_inversions = 0
                for i in range(n):
                    if i < l or i > r:
                        # Elements outside the transformed segment are not affected by the operation
                        continue
                    if permutation[i] > permutation[l + p - 1]:
                        transformed_inversions += 1

                # Add the probability of this transformation to the expected number of inversions
                expected_inversions += (transformed_inversions - inversions) / k

    return expected_inversions

