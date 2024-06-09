
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

def get_absolute_difference(a, b):
    return abs(a - b)

def main():
    n = int(input())
    permutations = get_permutations(n)
    lexicographically_smallest_permutations = get_lexicographically_smallest_permutations(permutations)
    a = lexicographically_smallest_permutations.index(input()) + 1
    b = lexicographically_smallest_permutations.index(input()) + 1
    absolute_difference = get_absolute_difference(a, b)
    print(absolute_difference)

if __name__ == '__main__':
    main()

