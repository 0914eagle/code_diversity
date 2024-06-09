
def get_rearranged_array(arr):
    n = len(arr)
    if n == 0:
        return []
    # sort the array
    arr.sort()
    # create a dictionary to store the counts of each element
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    # create a list to store the rearranged array
    rearranged_arr = []
    # iterate through the dictionary and add elements to the rearranged array
    for num in counts:
        for i in range(counts[num]):
            rearranged_arr.append(num)
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
    # create a dictionary to store the counts of each element
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    # check if there is at least one element with a count greater than 1
    has_duplicates = False
    for num in counts:
        if counts[num] > 1:
            has_duplicates = True
            break
    if not has_duplicates:
        return "NO"
    # create a list to store the rearranged array
    rearranged_arr = []
    # iterate through the dictionary and add elements to the rearranged array
    for num in counts:
        for i in range(counts[num]):
            rearranged_arr.append(num)
    # check if the rearranged array has a nonzero sum for all k
    for k in range(1, n+1):
        if not has_nonzero_sum(rearranged_arr, k):
            return "NO"
    return "YES\n" + str(rearranged_arr)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))

