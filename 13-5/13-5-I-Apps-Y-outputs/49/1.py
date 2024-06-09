
def f1(n):
    # f1 function to find the final value of the array after applying the algorithm
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == 1:
            a[i] = 2
        elif a[i] == 2:
            a[i] = 1
        elif a[i] == 3:
            a[i] = 4
        elif a[i] == 4:
            a[i] = 3
        elif a[i] == 5:
            a[i] = 6
        elif a[i] == 6:
            a[i] = 5
        elif a[i] == 7:
            a[i] = 8
        elif a[i] == 8:
            a[i] = 7
        elif a[i] == 9:
            a[i] = 10
        elif a[i] == 10:
            a[i] = 9
    return a

def f2(n):
    # f2 function to find the final value of the array after applying the algorithm for each pair of adjacent integers
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == 1:
            a[i] = 2
        elif a[i] == 2:
            a[i] = 1
        elif a[i] == 3:
            a[i] = 4
        elif a[i] == 4:
            a[i] = 3
        elif a[i] == 5:
            a[i] = 6
        elif a[i] == 6:
            a[i] = 5
        elif a[i] == 7:
            a[i] = 8
        elif a[i] == 8:
            a[i] = 7
        elif a[i] == 9:
            a[i] = 10
        elif a[i] == 10:
            a[i] = 9
    return a

if __name__ == '__main__':
    n = int(input())
    print(*f2(n), sep='\n')

