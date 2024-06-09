
def get_max_product(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # find the index of the first negative number
    neg_idx = 0
    while arr[neg_idx] < 0:
        neg_idx += 1
    
    # find the index of the first positive number
    pos_idx = neg_idx + 1
    while arr[pos_idx] > 0:
        pos_idx += 1
    
    # find the maximum product of the first negative number and the first positive number
    max_prod = arr[neg_idx] * arr[pos_idx]
    
    # find the maximum product of the first negative number and the second positive number
    if pos_idx + 1 < n and arr[pos_idx + 1] > 0:
        max_prod = max(max_prod, arr[neg_idx] * arr[pos_idx + 1])
    
    # find the maximum product of the second negative number and the first positive number
    if neg_idx + 1 < n and arr[neg_idx + 1] < 0:
        max_prod = max(max_prod, arr[neg_idx + 1] * arr[pos_idx])
    
    # find the maximum product of the second negative number and the second positive number
    if neg_idx + 1 < n and pos_idx + 1 < n and arr[neg_idx + 1] < 0 and arr[pos_idx + 1] > 0:
        max_prod = max(max_prod, arr[neg_idx + 1] * arr[pos_idx + 1])
    
    return max_prod

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_product(arr))

if __name__ == '__main__':
    main()

