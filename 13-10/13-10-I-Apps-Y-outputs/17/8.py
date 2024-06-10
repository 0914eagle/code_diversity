
def lexicographically_smaller(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return a[i] < b[i]
    return False

def find_lexicographically_smallest(permutation):
    smallest = permutation
    for i in range(len(permutation)):
        for j in range(i+1, len(permutation)):
            if lexicographically_smaller(permutation[i], permutation[j]):
                smallest = permutation[i]
    return smallest

def find_lexicographically_largest(permutation):
    largest = permutation
    for i in range(len(permutation)):
        for j in range(i+1, len(permutation)):
            if lexicographically_smaller(permutation[j], permutation[i]):
                largest = permutation[j]
    return largest

def find_index_lexicographically_smallest(permutation):
    index = 1
    for i in range(len(permutation)):
        if permutation == find_lexicographically_smallest(permutation[:i] + permutation[i+1:]):
            return index
        index += 1
    return index

def find_index_lexicographically_largest(permutation):
    index = 1
    for i in range(len(permutation)):
        if permutation == find_lexicographically_largest(permutation[:i] + permutation[i+1:]):
            return index
        index += 1
    return index

def find_abs_diff_index(p, q):
    return abs(find_index_lexicographically_smallest(p) - find_index_lexicographically_largest(q))

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(find_abs_diff_index(p, q))

