
def f1(n, v, a, b):
    # find the direct supervisor of each employee
    supervisor = [0] * (n + 1)
    for i in range(len(a)):
        supervisor[a[i]] = b[i]
    
    # find the set of jokes told by each employee and their supervisor
    jokes = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        jokes[i].add(v[i - 1])
        if supervisor[i] != 0:
            jokes[i].update(jokes[supervisor[i]])
    
    # count the number of different sets of jokes
    num_sets = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if len(jokes[i].symmetric_difference(jokes[j])) == 0:
                num_sets += 1
    
    return num_sets

def f2(n, v, a, b):
    # find the direct supervisor of each employee
    supervisor = [0] * (n + 1)
    for i in range(len(a)):
        supervisor[a[i]] = b[i]
    
    # find the set of jokes told by each employee and their supervisor
    jokes = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        jokes[i].add(v[i - 1])
        if supervisor[i] != 0:
            jokes[i].update(jokes[supervisor[i]])
    
    # count the number of different sets of jokes
    num_sets = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if len(jokes[i].symmetric_difference(jokes[j])) == 0:
                num_sets += 1
    
    return num_sets

if __name__ == '__main__':
    n = int(input())
    v = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(n, v, a, b))
    print(f2(n, v, a, b))

