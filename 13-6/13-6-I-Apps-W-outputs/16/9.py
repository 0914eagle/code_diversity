
def get_pairs(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

def get_array(n):
    return [i for i in range(1, n+1)]

def get_unique_elements(array):
    return len(set(array))

def get_function(array):
    return lambda x, y: x + y

def get_result(array, pairs, function):
    result = []
    for pair in pairs:
        x, y = pair
        t = function(array[x-1], array[y-1])
        array[x-1] = t
        array[y-1] = t
        result.append(t)
    return result

def main():
    n = int(input())
    pairs = get_pairs(n)
    array = get_array(n)
    function = get_function(array)
    result = get_result(array, pairs, function)
    unique_elements = get_unique_elements(result)
    if unique_elements <= 2:
        print(len(pairs))
        for pair in pairs:
            print(*pair)
    else:
        print(-1)

if __name__ == '__main__':
    main()

