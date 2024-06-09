
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
    # Replace all occurrences of 7 with 8
    a = [8 if x == 7 else x for x in a]
    # Replace all occurrences of 8 with 7
    a = [7 if x == 8 else x for x in a]
    # Replace all occurrences of 9 with 10
    a = [10 if x == 9 else x for x in a]
    # Replace all occurrences of 10 with 9
    a = [9 if x == 10 else x for x in a]
    return a

def f2(n, a):
    # Replace all occurrences of 11 with 12
    a = [12 if x == 11 else x for x in a]
    # Replace all occurrences of 12 with 11
    a = [11 if x == 12 else x for x in a]
    # Replace all occurrences of 13 with 14
    a = [14 if x == 13 else x for x in a]
    # Replace all occurrences of 14 with 13
    a = [13 if x == 14 else x for x in a]
    # Replace all occurrences of 15 with 16
    a = [16 if x == 15 else x for x in a]
    # Replace all occurrences of 16 with 15
    a = [15 if x == 16 else x for x in a]
    # Replace all occurrences of 17 with 18
    a = [18 if x == 17 else x for x in a]
    # Replace all occurrences of 18 with 17
    a = [17 if x == 18 else x for x in a]
    # Replace all occurrences of 19 with 20
    a = [20 if x == 19 else x for x in a]
    # Replace all occurrences of 20 with 19
    a = [19 if x == 20 else x for x in a]
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*f1(n, a))
    print(*f2(n, a))

