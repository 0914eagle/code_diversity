
def get_pairs(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

def get_array(n):
    array = [i for i in range(1, n+1)]
    return array

def get_function(n):
    def f(x, y):
        return x*y
    return f

def get_solution(n):
    pairs = get_pairs(n)
    array = get_array(n)
    f = get_function(n)
    for pair in pairs:
        x, y = pair
        t = f(array[x], array[y])
        array[x] = t
        array[y] = t
    return array

if __name__ == '__main__':
    n = int(input())
    solution = get_solution(n)
    print(len(set(solution)))
    for i in range(len(solution)):
        print(solution[i], end=" ")

