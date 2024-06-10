
def get_input():
    n = int(input())
    return n

def get_permutations(n):
    permutations = []
    for i in range(n+1):
        permutations.append(i)
    return permutations

def get_beauty(permutation):
    beauty = 0
    for i in range(len(permutation)):
        beauty += (i ^ permutation[i])
    return beauty

def get_max_beauty(permutations):
    max_beauty = 0
    max_permutation = []
    for permutation in permutations:
        beauty = get_beauty(permutation)
        if beauty > max_beauty:
            max_beauty = beauty
            max_permutation = permutation
    return max_beauty, max_permutation

def print_output(max_beauty, max_permutation):
    print(max_beauty)
    print(' '.join(map(str, max_permutation)))

if __name__ == '__main__':
    n = get_input()
    permutations = get_permutations(n)
    max_beauty, max_permutation = get_max_beauty(permutations)
    print_output(max_beauty, max_permutation)

