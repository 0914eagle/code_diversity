
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
            for p in permutations(range(1, k + 1)):
                # Calculate the number of inversions in the transformed permutation
                transformed_inversions = 0
                for i in range(n):
                    if i < l or i > r:
                        # Elements before l and after r are not affected by the operation
                        continue
                    transformed_index = l + p.index(i - l + 1)
                    if transformed_index < i:
                        # Elements before the transformed index are not affected by the operation
                        continue
                    if permutation[transformed_index] > permutation[i]:
                        transformed_inversions += 1

                # Add the number of inversions for this operation to the expected number of inversions
                expected_inversions += transformed_inversions

    # Return the expected number of inversions
    return expected_inversions / n / (n - 1)

