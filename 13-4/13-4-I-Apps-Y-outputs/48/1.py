
def get_permutations(n):
    permutations = []
    for i in range(1, n+1):
        permutations.append(i)
    return permutations

def get_lexicographically_smallest_permutation(permutations):
    return permutations

def get_lexicographically_largest_permutation(permutations):
    return permutations[::-1]

def get_absolute_difference(a, b):
    return abs(a - b)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    permutations = get_permutations(n)
    a = get_lexicographically_smallest_permutation(permutations).index(p) + 1
    b = get_lexicographically_smallest_permutation(permutations).index(q) + 1
    print(get_absolute_difference(a, b))

if __name__ == '__main__':
    main()

