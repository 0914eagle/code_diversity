
def get_max_product(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # sort the array in non-decreasing order
    arr.sort()
    
    # find the index of the first negative number
    i = 0
    while i < n and arr[i] > 0:
        i += 1
    
    # if there are no negative numbers, return the array as is
    if i == n:
        return arr
    
    # find the index of the first positive number after the first negative number
    j = i + 1
    while j < n and arr[j] < 0:
        j += 1
    
    # if there are no positive numbers after the first negative number, return the array as is
    if j == n:
        return arr
    
    # swap the first negative number with the first positive number
    arr[i], arr[j] = arr[j], arr[i]
    
    # reverse the order of the elements after the first negative number
    arr[i+1:] = arr[i+1:][::-1]
    
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*get_max_product(arr))

if __name__ == '__main__':
    main()

