
def get_permutation_index(perm):
    n = len(perm)
    index = 1
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                index += 1
    return index

def get_absolute_difference(p, q):
    p_index = get_permutation_index(p)
    q_index = get_permutation_index(q)
    return abs(p_index - q_index)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(get_absolute_difference(p, q))

if __name__ == '__main__':
    main()

