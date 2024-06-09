
def find_pairs(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

def find_solution(n):
    pairs = find_pairs(n)
    array = [i for i in range(1, n+1)]
    for pair in pairs:
        x, y = pair
        t = f(array[x], array[y])
        array[x] = t
        array[y] = t
    return array

def f(a, b):
    return a + b

if __name__ == '__main__':
    n = int(input())
    array = find_solution(n)
    print(len(set(array)))
    for i in range(1, n+1):
        if array[i] != array[i-1]:
            print(i, i+1)
            break

