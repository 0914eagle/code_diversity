
def f1(n, a):
    # Check if the list is already sorted
    if a == sorted(a):
        return "impossible"
    
    # Find the index of the first number that is not in sorted order
    i = 0
    while i < n-1 and a[i] <= a[i+1]:
        i += 1
    
    # If all numbers are in sorted order, return impossible
    if i == n-1:
        return "impossible"
    
    # Find the index of the number to change
    j = i+1
    while j < n and a[j] <= a[i]:
        j += 1
    
    # Change the number at index i to be equal to the number at index j
    a[i] = a[j]
    
    # Return the resulting list
    return a

def f2(n, a):
    # Check if the list is already sorted
    if a == sorted(a):
        return "impossible"
    
    # Find the index of the first number that is not in sorted order
    i = 0
    while i < n-1 and a[i] <= a[i+1]:
        i += 1
    
    # If all numbers are in sorted order, return impossible
    if i == n-1:
        return "impossible"
    
    # Find the index of the number to change
    j = i+1
    while j < n and a[j] <= a[i]:
        j += 1
    
    # Change the number at index i to be equal to the number at index j
    a[i] = a[j]
    
    # Return the resulting list
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

