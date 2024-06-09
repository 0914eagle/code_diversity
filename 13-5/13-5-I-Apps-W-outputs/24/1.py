
def f1(n, a):
    # f1(n, a) should return the initial order of the cubes
    # n: the number of cubes
    # a: the current order of the cubes
    
    # reverse the array
    a = a[::-1]
    
    # reverse the first half of the array
    a[:n//2] = a[:n//2][::-1]
    
    # reverse the second half of the array
    a[n//2:] = a[n//2:][::-1]
    
    return a
    
def f2(n, a):
    # f2(n, a) should return the initial order of the cubes
    # n: the number of cubes
    # a: the current order of the cubes
    
    # find the middle index
    mid = n//2
    
    # reverse the array from mid to the end
    a[mid:] = a[mid:][::-1]
    
    return a
    
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*f1(n, a))

