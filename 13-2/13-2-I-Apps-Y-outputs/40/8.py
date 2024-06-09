
def f1(n, a):
    # Sort the array in ascending order
    a.sort()
    
    # Initialize the number of pockets as 1
    pockets = 1
    
    # Iterate through the array
    for i in range(n-1):
        # If the current value is different from the previous value, increment the number of pockets
        if a[i] != a[i+1]:
            pockets += 1
    
    return pockets

def f2(n, a):
    # Sort the array in descending order
    a.sort(reverse=True)
    
    # Initialize the number of pockets as 1
    pockets = 1
    
    # Iterate through the array
    for i in range(n-1):
        # If the current value is different from the previous value, increment the number of pockets
        if a[i] != a[i+1]:
            pockets += 1
    
    return pockets

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(min(f1(n, a), f2(n, a)))

