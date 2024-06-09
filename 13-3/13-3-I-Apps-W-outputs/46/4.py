
def f1(n, a, b):
    # find the k value that maximizes the number of finalists
    k = 0
    while k < n:
        finalists = a[:k] + b[n-k:]
        if len(set(finalists)) == n:
            break
        k += 1
    
    # create a list of booleans indicating whether a participant has any chance to advance to the finals
    has_chance = [False] * n
    for i in range(k):
        has_chance[i] = True
    for i in range(n-k):
        has_chance[a[i]] = True
        has_chance[b[i]] = True
    
    return ''.join('1' if has_chance[i] else '0' for i in range(n))

def f2(n, a, b):
    # find the k value that maximizes the number of finalists
    k = 0
    while k < n:
        finalists = a[:k] + b[n-k:]
        if len(set(finalists)) == n:
            break
        k += 1
    
    # create a list of booleans indicating whether a participant has any chance to advance to the finals
    has_chance = [False] * n
    for i in range(k):
        has_chance[i] = True
    for i in range(n-k):
        has_chance[a[i]] = True
        has_chance[b[i]] = True
    
    return ''.join('1' if has_chance[i] else '0' for i in range(n))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(n, a, b))
    print(f2(n, a, b))

