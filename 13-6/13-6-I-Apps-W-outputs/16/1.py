
def get_pairs(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

def get_array(n):
    array = [i for i in range(1, n+1)]
    return array

def get_function(array, pairs):
    function = {}
    for i, j in pairs:
        function[i, j] = array[i-1] + array[j-1]
    return function

def get_new_array(array, function):
    new_array = []
    for i in range(len(array)):
        new_array.append(function[i+1, i+1])
    return new_array

def get_unique_elements(array):
    unique_elements = set()
    for element in array:
        unique_elements.add(element)
    return len(unique_elements)

def main():
    n = int(input())
    pairs = get_pairs(n)
    array = get_array(n)
    function = get_function(array, pairs)
    new_array = get_new_array(array, function)
    unique_elements = get_unique_elements(new_array)
    print(len(pairs))
    for i, j in pairs:
        print(i, j)

if __name__ == '__main__':
    main()

