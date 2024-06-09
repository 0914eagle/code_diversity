
def f1(n, a):
    # Replace all occurrences of 1 with 2
    a = [x if x != 1 else 2 for x in a]
    return a

def f2(n, a):
    # Replace all occurrences of 2 with 1
    a = [x if x != 2 else 1 for x in a]
    return a

def f3(n, a):
    # Replace all occurrences of 3 with 4
    a = [x if x != 3 else 4 for x in a]
    return a

def f4(n, a):
    # Replace all occurrences of 4 with 3
    a = [x if x != 4 else 3 for x in a]
    return a

def f5(n, a):
    # Replace all occurrences of 5 with 6
    a = [x if x != 5 else 6 for x in a]
    return a

def f6(n, a):
    # Replace all occurrences of 6 with 5
    a = [x if x != 6 else 5 for x in a]
    return a

def f7(n, a):
    # Replace all occurrences of 7 with 8
    a = [x if x != 7 else 8 for x in a]
    return a

def f8(n, a):
    # Replace all occurrences of 8 with 7
    a = [x if x != 8 else 7 for x in a]
    return a

def f9(n, a):
    # Replace all occurrences of 9 with 10
    a = [x if x != 9 else 10 for x in a]
    return a

def f10(n, a):
    # Replace all occurrences of 10 with 9
    a = [x if x != 10 else 9 for x in a]
    return a

def apply_algorithm(n, a):
    # Apply the algorithm to the array a
    for i in range(1, 10**8+1):
        a = f1(n, a)
        a = f2(n, a)
        a = f3(n, a)
        a = f4(n, a)
        a = f5(n, a)
        a = f6(n, a)
        a = f7(n, a)
        a = f8(n, a)
        a = f9(n, a)
        a = f10(n, a)
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*apply_algorithm(n, a))

