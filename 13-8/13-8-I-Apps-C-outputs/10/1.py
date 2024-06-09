
def get_min_mex(subarrays):
    mex = 0
    for subarray in subarrays:
        for i in range(subarray[0], subarray[1] + 1):
            if i not in subarray:
                if mex < i:
                    mex = i
                break
    return mex

def get_optimal_array(n, m):
    subarrays = []
    for i in range(m):
        l, r = map(int, input().split())
        subarrays.append((l, r))
    
    a = [0] * n
    for i in range(n):
        a[i] = i + 1
    
    min_mex = get_min_mex(subarrays)
    for i in range(n):
        if a[i] < min_mex:
            a[i] = min_mex
    
    return a

n, m = map(int, input().split())
a = get_optimal_array(n, m)
print(min_mex)
print(*a)

