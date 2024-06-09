
def f1(n, a):
    # Replace all occurrences of 1 with 2
    a = [2 if x == 1 else x for x in a]
    # Replace all occurrences of 2 with 1
    a = [1 if x == 2 else x for x in a]
    # Replace all occurrences of 3 with 4
    a = [4 if x == 3 else x for x in a]
    # Replace all occurrences of 4 with 3
    a = [3 if x == 4 else x for x in a]
    # Replace all occurrences of 5 with 6
    a = [6 if x == 5 else x for x in a]
    # Replace all occurrences of 6 with 5
    a = [5 if x == 6 else x for x in a]
    # Replace all occurrences of 10 with 9
    a = [9 if x == 10 else x for x in a]
    return a

def f2(n, a):
    # Apply the algorithm for each pair of adjacent integers (2i - 1, 2i)
    for i in range(1, 500000001):
        a = f1(n, a)
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*f2(n, a))

