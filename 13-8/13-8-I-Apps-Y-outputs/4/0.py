
def get_permutations(n):
    permutations = []
    for i in range(1, n+1):
        permutations.append(i)
    return permutations

def get_lexicographically_smallest_permutations(permutations):
    lexicographically_smallest_permutations = []
    for i in range(len(permutations)):
        lexicographically_smallest_permutations.append(permutations[i])
    return lexicographically_smallest_permutations

def get_a_b(permutations, lexicographically_smallest_permutations):
    a = lexicographically_smallest_permutations.index(permutations[0]) + 1
    b = lexicographically_smallest_permutations.index(permutations[1]) + 1
    return a, b

def main():
    n = int(input())
    permutations = get_permutations(n)
    lexicographically_smallest_permutations = get_lexicographically_smallest_permutations(permutations)
    a, b = get_a_b(permutations, lexicographically_smallest_permutations)
    print(abs(a - b))

if __name__ == '__main__':
    main()

