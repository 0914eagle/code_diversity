
def get_permutation_beauty(permutation):
    # Calculate the beauty of the permutation
    beauty = 0
    for i in range(len(permutation)):
        beauty += (i ^ permutation[i])
    return beauty

def get_max_beauty_permutation(n):
    # Generate all permutations of integers from 0 to n
    permutations = []
    for i in range(n+1):
        permutations.append(i)
    permutations = list(permutations)
    for i in range(n):
        for j in range(i+1, n+1):
            permutations[i], permutations[j] = permutations[j], permutations[i]
            permutations = list(permutations)
    # Find the permutation with the maximum beauty
    max_beauty = 0
    max_permutation = []
    for permutation in permutations:
        beauty = get_permutation_beauty(permutation)
        if beauty > max_beauty:
            max_beauty = beauty
            max_permutation = permutation
    return max_permutation

if __name__ == '__main__':
    n = int(input())
    permutation = get_max_beauty_permutation(n)
    print(get_permutation_beauty(permutation))
    print(*permutation)

