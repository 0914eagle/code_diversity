
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
    # loop through the dictionary and add the elements to the new array
    for key in freq:
        for i in range(freq[key]):
            rearranged_arr.append(key)
    return rearranged_arr

def has_nonzero_sum(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] != 0:
                return True
    return False

def solve(arr):
    rearranged_arr = get_rearranged_array(arr)
    if has_nonzero_sum(rearranged_arr):
        return "YES\n" + str(rearranged_arr)
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))

