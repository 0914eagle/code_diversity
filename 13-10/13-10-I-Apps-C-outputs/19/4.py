
def get_maximum(a, k):
    n = len(a)
    if k >= n:
        return sum(a)
    
    # sort the array in non-decreasing order
    a.sort()
    
    # initialize the maximum value of m(a)
    max_value = sum(a)
    
    # loop through all possible pairs of indices
    for i in range(n-1):
        for j in range(i+1, n):
            # check if the swap operation increases the maximum value of m(a)
            if a[i] + a[j] > max_value:
                # perform the swap operation
                a[i], a[j] = a[j], a[i]
                # update the maximum value of m(a)
                max_value = sum(a)
                # undo the swap operation
                a[i], a[j] = a[j], a[i]
    
    return max_value

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum(a, k))

if __name__ == '__main__':
    main()

