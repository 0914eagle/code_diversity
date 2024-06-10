
def get_permutation(n):
    permutation = list(map(int, input().split()))
    return permutation

def is_sorted(permutation):
    return permutation == list(range(1, len(permutation) + 1))

def swap_elements(permutation, i, j):
    permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation

def can_sort_permutation(permutation):
    n = len(permutation)
    for i in range(n):
        for j in range(i+1, n):
            if permutation[i] > permutation[j]:
                permutation = swap_elements(permutation, i, j)
    return is_sorted(permutation)

def main():
    n = int(input())
    permutation = get_permutation(n)
    if can_sort_permutation(permutation):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

