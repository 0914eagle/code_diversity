
def get_lexicographical_index(permutation):
    
    index = 1
    for i in range(1, len(permutation)):
        for j in range(i):
            if permutation[i] < permutation[j]:
                index += 1
    return index

def get_absolute_difference(p, q):
    
    a = get_lexicographical_index(p)
    b = get_lexicographical_index(q)
    return abs(a - b)

if __name__ == '__main__':
    N = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(get_absolute_difference(p, q))

