
def f1(n, a):
    # f1(n, a) should return the initial order of the cubes
    # based on the current order a
    
    # reverse the order of the cubes
    a = a[::-1]
    
    # find the middle index
    mid = n // 2
    
    # reverse the order of the cubes from mid to the end
    a[mid:] = a[mid:][::-1]
    
    # return the initial order of the cubes
    return a

