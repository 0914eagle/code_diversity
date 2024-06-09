
def find_pairs(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

def find_array(n, pairs):
    array = [i for i in range(1, n+1)]
    for pair in pairs:
        x, y = pair
        array[x-1] = array[y-1]
    return array

def find_unique_elements(array):
    return len(set(array))

def main():
    n = int(input())
    pairs = find_pairs(n)
    array = find_array(n, pairs)
    unique_elements = find_unique_elements(array)
    print(unique_elements)
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == '__main__':
    main()

