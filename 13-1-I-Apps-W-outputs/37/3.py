
def solve(n, permutation):
    # Calculate the number of inversions in the original permutation
    inversions = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                inversions += 1

    # Calculate the expected number of inversions after applying the operation
    expected_inversions = 0
    for l in range(n):
        for r in range(l, n):
            k = r - l + 1
            for p in permutations(range(1, k + 1)):
                # Calculate the number of inversions in the transformed permutation
                transformed_inversions = 0
                for i in range(n):
                    if i < l or i > r:
                        continue
                    if permutation[i] > permutation[i + 1]:
                        transformed_inversions += 1

                # Add the contribution of this permutation to the expected number of inversions
                expected_inversions += transformed_inversions / math.factorial(k)

    return expected_inversions

