
def get_permutation_index(permutation, index):
    
    permutation_list = list(permutations(range(1, N + 1)))
    return permutation_list.index(permutation) + 1

def get_lexicographically_smaller_index(permutation1, permutation2):
    
    permutation1_list = list(permutation1)
    permutation2_list = list(permutation2)
    for i in range(N):
        if permutation1_list[i] != permutation2_list[i]:
            return permutation1_list[i]
    return -1

def solve(permutation1, permutation2):
    
    index1 = get_permutation_index(permutation1, N)
    index2 = get_permutation_index(permutation2, N)
    return abs(index1 - index2)

if __name__ == '__main__':
    N = int(input())
    permutation1 = tuple(map(int, input().split()))
    permutation2 = tuple(map(int, input().split()))
    print(solve(permutation1, permutation2))

