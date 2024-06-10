
def get_permutations(n):
    permutations = []
    for i in range(n+1):
        permutations.append(list(range(n+1)))
    return permutations

def get_beauty(permutation):
    beauty = 0
    for i in range(len(permutation)):
        beauty += (i ^ permutation[i])
    return beauty

def get_maximum_beauty_permutation(n):
    permutations = get_permutations(n)
    maximum_beauty = 0
    maximum_beauty_permutation = []
    for permutation in permutations:
        beauty = get_beauty(permutation)
        if beauty > maximum_beauty:
            maximum_beauty = beauty
            maximum_beauty_permutation = permutation
    return maximum_beauty, maximum_beauty_permutation

if __name__ == '__main__':
    n = int(input())
    maximum_beauty, maximum_beauty_permutation = get_maximum_beauty_permutation(n)
    print(maximum_beauty)
    print(*maximum_beauty_permutation)

