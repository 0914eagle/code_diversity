
def f1(n, v, a, b):
    # find the direct supervisor of each person
    supervisor = [0] * (n + 1)
    for i in range(len(a)):
        supervisor[a[i]] = b[i]
    
    # find the set of jokes told by each person and their supervisor
    jokes = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        jokes[i].add(v[i - 1])
        if supervisor[i] != 0:
            jokes[i].update(jokes[supervisor[i]])
    
    # count the number of different sets of jokes
    num_sets = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if jokes[i].isdisjoint(jokes[j]):
                num_sets += 1
    
    return num_sets

def f2(n, v, a, b):
    # find the direct supervisor of each person
    supervisor = [0] * (n + 1)
    for i in range(len(a)):
        supervisor[a[i]] = b[i]
    
    # find the set of jokes told by each person and their supervisor
    jokes = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        jokes[i].add(v[i - 1])
        if supervisor[i] != 0:
            jokes[i].update(jokes[supervisor[i]])
    
    # count the number of different sets of jokes
    num_sets = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if jokes[i].isdisjoint(jokes[j]):
                num_sets += 1
    
    return num_sets

if __name__ == '__main__':
    n = int(input())
    v = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(n, v, a, b))
    print(f2(n, v, a, b))

