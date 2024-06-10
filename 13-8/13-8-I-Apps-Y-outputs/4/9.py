
def get_lexicographically_smallest_permutations(permutation):
    permutations = []
    for i in range(1, len(permutation) + 1):
        permutations.append(list(permutation[:i]))
    permutations.sort()
    return permutations

def get_absolute_difference_of_lexicographically_smallest_permutations(permutation1, permutation2):
    permutations1 = get_lexicographically_smallest_permutations(permutation1)
    permutations2 = get_lexicographically_smallest_permutations(permutation2)
    return abs(permutations1.index(permutation1) - permutations2.index(permutation2))

if __name__ == '__main__':
    n = int(input())
    permutation1 = list(map(int, input().split()))
    permutation2 = list(map(int, input().split()))
    print(get_absolute_difference_of_lexicographically_smallest_permutations(permutation1, permutation2))

