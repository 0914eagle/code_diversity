
def get_permutations(n):
    permutations = []
    for i in range(n+1):
        permutations.append(list(i for i in range(n+1)))
    return permutations

def get_beauty(permutation):
    beauty = 0
    for i in range(len(permutation)):
        beauty += (i ^ permutation[i])
    return beauty

def find_max_beauty_permutation(n):
    permutations = get_permutations(n)
    max_beauty = 0
    max_permutation = []
    for permutation in permutations:
        beauty = get_beauty(permutation)
        if beauty > max_beauty:
            max_beauty = beauty
            max_permutation = permutation
    return max_permutation

if __name__ == '__main__':
    n = int(input())
    max_permutation = find_max_beauty_permutation(n)
    print(get_beauty(max_permutation))
    print(*max_permutation)

