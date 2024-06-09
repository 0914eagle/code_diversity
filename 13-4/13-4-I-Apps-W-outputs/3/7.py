
def solve(n, permutation, target_permutation):
    # Convert the permutations to lists
    permutation = list(permutation)
    target_permutation = list(target_permutation)

    # Check if the target permutation is a rotation of the original permutation
    if target_permutation == permutation[n-3:] + permutation[:n-3]:
        return "Possible"
    else:
        return "Impossible"

