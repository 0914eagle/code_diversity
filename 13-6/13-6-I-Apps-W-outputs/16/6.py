
def find_pairs(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

def perform_operations(pairs, n):
    array = [i for i in range(1, n+1)]
    for i, j in pairs:
        t = f(array[i-1], array[j-1])
        array[i-1] = t
        array[j-1] = t
    return array

def f(x, y):
    return x+y

if __name__ == '__main__':
    n = int(input())
    pairs = find_pairs(n)
    array = perform_operations(pairs, n)
    print(len(set(array)))
    for i in range(1, n+1):
        if array[i-1] in set(array[:i-1]):
            print(i, array[i-1])
            break

