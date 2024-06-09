
def cyclic_shift(word):
    n = len(word)
    result = set()
    result.add(word)
    for i in range(n):
        result.add(word[i:] + word[:i])
    return len(result)

def f1(...):
    ...
    return ...

def f2(...):
    ...
    return ...

if __name__ == '__main__':
    word = input()
    print(cyclic_shift(word))

