
def get_lexicographical_index(permutation):
    
    n = len(permutation)
    index = 0
    for i in range(n):
        for j in range(i+1, n):
            if permutation[i] > permutation[j]:
                index += 1
    return index

def get_permutation_count(n):
    
    return math.factorial(n)

def get_difference(p, q):
    
    return abs(get_lexicographical_index(p) - get_lexicographical_index(q))

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(get_difference(p, q))

