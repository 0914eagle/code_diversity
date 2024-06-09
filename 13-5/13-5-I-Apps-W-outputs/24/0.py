
def f1(n, arr):
    # f1 function should take two arguments: n (the number of cubes) and arr (the current order of the cubes)
    # f1 function should return the initial order of the cubes
    
    # your code here
    return arr

def f2(n, arr):
    # f2 function should take two arguments: n (the number of cubes) and arr (the current order of the cubes)
    # f2 function should return the initial order of the cubes
    
    # your code here
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(*f1(n, arr))

