
def is_possible(n, k, a):
    # Check if all elements are already equal to k
    if all(x == k for x in a):
        return "yes"
    
    # Check if the sum of all elements is less than k
    if sum(a) < k:
        return "no"
    
    # Check if the median of the array is equal to k
    if median(a) == k:
        return "yes"
    
    # Check if the median of the array is greater than k
    if median(a) > k:
        # Find the index of the first element that is greater than k
        i = 0
        while i < n and a[i] > k:
            i += 1
        
        # Check if the sum of the elements before the first element that is greater than k is less than k
        if sum(a[:i]) < k:
            return "no"
    
    # Check if the median of the array is less than k
    if median(a) < k:
        # Find the index of the first element that is less than k
        i = 0
        while i < n and a[i] < k:
            i += 1
        
        # Check if the sum of the elements before the first element that is less than k is greater than k
        if sum(a[:i]) > k:
            return "no"
    
    return "yes"

def median(a):
    a.sort()
    if len(a) % 2 == 0:
        return (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2
    else:
        return a[len(a) // 2]

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(is_possible(n, k, a))

