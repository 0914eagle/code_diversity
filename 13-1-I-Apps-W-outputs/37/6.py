
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
                        # Elements before the segment are not affected by the operation
                        continue
                    elif i == l:
                        # The first element of the segment is transformed to p[1]
                        if permutation[i] > permutation[i + 1]:
                            transformed_inversions += 1
                    elif i == r:
                        # The last element of the segment is transformed to p[k]
                        if permutation[i - 1] > permutation[i]:
                            transformed_inversions += 1
                    else:
                        # Elements in the middle of the segment are transformed to p[i - l + 1]
                        if permutation[i - 1] > permutation[i]:
                            transformed_inversions += 1

                # Add the expected number of inversions for this transformed permutation to the total
                expected_inversions += transformed_inversions / k

    return expected_inversions

