
def get_permutations(n):
    permutations = []
    for i in range(1, n+1):
        permutations.append(i)
    return permutations

def get_lexicographically_smallest_permutation(permutations):
    permutations.sort()
    return permutations

def get_lexicographically_largest_permutation(permutations):
    permutations.sort(reverse=True)
    return permutations

def get_absolute_difference(a, b):
    return abs(a - b)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    permutations = get_permutations(n)
    p_lexicographically_smallest = get_lexicographically_smallest_permutation(p)
    q_lexicographically_smallest = get_lexicographically_smallest_permutation(q)
    p_lexicographically_largest = get_lexicographically_largest_permutation(p)
    q_lexicographically_largest = get_lexicographically_largest_permutation(q)
    a = permutations.index(p_lexicographically_smallest) + 1
    b = permutations.index(q_lexicographically_smallest) + 1
    c = permutations.index(p_lexicographically_largest) + 1
    d = permutations.index(q_lexicographically_largest) + 1
    print(get_absolute_difference(a, b))
    print(get_absolute_difference(c, d))

if __name__ == '__main__':
    main()

