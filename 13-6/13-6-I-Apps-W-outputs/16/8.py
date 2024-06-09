
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
    def f(x, y):
        return x + y
    return f

def perform_operations(pairs, array):
    for pair in pairs:
        x, y = pair
        t = array[x-1] + array[y-1]
        array[x-1] = t
        array[y-1] = t
    return array

def get_unique_elements_after_operations(array):
    return len(set(array))

def main():
    n = int(input())
    pairs = get_pairs(n)
    array = get_array(n)
    function = get_function(array)
    array = perform_operations(pairs, array)
    unique_elements = get_unique_elements_after_operations(array)
    print(unique_elements)
    for pair in pairs:
        print(*pair)

if __name__ == '__main__':
    main()

