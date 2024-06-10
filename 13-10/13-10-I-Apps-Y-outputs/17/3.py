
def get_permutations(n):
    permutations = []
    for i in range(1, n+1):
        permutations.append(i)
    return permutations

def get_lexicographically_smallest(permutations):
    permutations.sort()
    return permutations

def get_lexicographically_largest(permutations):
    permutations.sort(reverse=True)
    return permutations

def get_position_of_permutation(permutation, all_permutations):
    for i, p in enumerate(all_permutations):
        if p == permutation:
            return i
    return -1

def get_absolute_difference(a, b):
    return abs(a - b)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    all_permutations = get_permutations(n)
    p_lexicographically_smallest = get_lexicographically_smallest(p)
    q_lexicographically_smallest = get_lexicographically_smallest(q)
    p_position = get_position_of_permutation(p_lexicographically_smallest, all_permutations)
    q_position = get_position_of_permutation(q_lexicographically_smallest, all_permutations)
    print(get_absolute_difference(p_position, q_position))

if __name__ == '__main__':
    main()

