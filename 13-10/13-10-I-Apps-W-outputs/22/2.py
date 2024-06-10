
def count_sorted_subarrays(arr, x):
    # Initialize a set to store the unique elements of the array
    unique_elements = set()
    # Iterate through the array and add each element to the set
    for element in arr:
        unique_elements.add(element)
    # Initialize a variable to store the count of sorted subarrays
    count = 0
    # Iterate through the range of possible values for l and r
    for l in range(1, x + 1):
        for r in range(l, x + 1):
            # Check if the subarray obtained by erasing all values such that l <= a[i] <= r is sorted
            if is_sorted_subarray(arr, l, r, unique_elements):
                count += 1
    return count

def is_sorted_subarray(arr, l, r, unique_elements):
    # Initialize a variable to store the count of unique elements in the subarray
    count = 0
    # Iterate through the array and check if each element is in the range l to r
    for element in arr:
        if l <= element <= r:
            count += 1
    # Return True if the count of unique elements is equal to the number of elements in the subarray
    return count == len(unique_elements)

if __name__ == '__main__':
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_sorted_subarrays(arr, x))

