
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

def get_max_beauty_permutation(n):
    permutations = get_permutations(n)
    max_beauty = 0
    max_beauty_permutation = []
    for permutation in permutations:
        beauty = get_beauty(permutation)
        if beauty > max_beauty:
            max_beauty = beauty
            max_beauty_permutation = permutation
    return max_beauty, max_beauty_permutation

def main():
    n = int(input())
    max_beauty, max_beauty_permutation = get_max_beauty_permutation(n)
    print(max_beauty)
    print(*max_beauty_permutation)

if __name__ == '__main__':
    main()

