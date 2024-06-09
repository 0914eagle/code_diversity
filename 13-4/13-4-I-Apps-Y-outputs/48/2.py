
def get_permutations(n):
    permutations = []
    for i in range(1, n+1):
        permutations.append(i)
    return permutations

def get_lexicographically_smallest_permutations(permutations):
    lexicographically_smallest_permutations = []
    for permutation in permutations:
        lexicographically_smallest_permutations.append(permutation)
    return lexicographically_smallest_permutations

def get_a_minus_b(permutations, a, b):
    a_index = permutations.index(a)
    b_index = permutations.index(b)
    return abs(a_index - b_index)

if __name__ == '__main__':
    n = int(input())
    permutations = get_permutations(n)
    lexicographically_smallest_permutations = get_lexicographically_smallest_permutations(permutations)
    a = lexicographically_smallest_permutations[1]
    b = lexicographically_smallest_permutations[2]
    print(get_a_minus_b(permutations, a, b))

