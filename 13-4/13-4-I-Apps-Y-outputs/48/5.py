
def get_lexicographical_index(permutation):
    
    n = len(permutation)
    index = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                index += 1
    return index

def get_absolute_difference(p, q):
    
    return abs(get_lexicographical_index(p) - get_lexicographical_index(q))

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(get_absolute_difference(p, q))

