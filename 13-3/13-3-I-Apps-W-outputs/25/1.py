
def get_rearranged_array(arr):
    # Sort the array
    arr.sort()
    # Create a new array with the same elements
    new_arr = arr[:]
    # Rearrange the elements
    for i in range(len(arr)):
        new_arr[i] = arr[(i+1) % len(arr)]
    return new_arr

def has_nonzero_sum(arr, k):
    # Calculate the sum of the first k elements
    sum = 0
    for i in range(k):
        sum += arr[i]
    # Return True if the sum is nonzero, False otherwise
    return sum != 0

def solve(arr):
    # Get a rearranged array
    new_arr = get_rearranged_array(arr)
    # Check if the sum of the first k elements is nonzero for all k
    for k in range(1, len(arr)+1):
        if not has_nonzero_sum(new_arr, k):
            return "NO"
    # If all sums are nonzero, return the rearranged array
    return "YES\n" + str(new_arr)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))

