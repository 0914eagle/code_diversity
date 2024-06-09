
def get_rearranged_array(arr):
    n = len(arr)
    if n == 0:
        return []
    # sort the array
    arr.sort()
    # create a dictionary to store the frequency of each element
    freq = {}
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1
    # create a new array to store the rearranged elements
    rearranged_arr = []
    # iterate through the dictionary and add the elements to the new array
    for key in freq:
        for i in range(freq[key]):
            rearranged_arr.append(key)
    return rearranged_arr

def has_nonzero_sum(arr, k):
    sum = 0
    for i in range(k):
        sum += arr[i]
    return sum != 0

def solve(arr):
    n = len(arr)
    # check if the array is empty
    if n == 0:
        return "NO"
    # sort the array
    arr.sort()
    # find the first element that has a non-zero sum
    for i in range(n):
        if has_nonzero_sum(arr, i+1):
            break
    # create a new array with the first element and the remaining elements
    rearranged_arr = [arr[i]] + arr[i+1:]
    # check if the rearranged array has a non-zero sum for all elements
    for i in range(n):
        if not has_nonzero_sum(rearranged_arr, i+1):
            return "NO"
    return "YES\n" + str(rearranged_arr)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))

