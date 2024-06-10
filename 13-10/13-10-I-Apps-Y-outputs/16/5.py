
def is_good_array(arr):
    # Check if the length of the array is divisible by 6
    if len(arr) % 6 != 0:
        return False
    
    # Check if the array can be split into 6 subsequences of length 2
    subseq_len = len(arr) // 6
    subseqs = [arr[i:i + subseq_len] for i in range(0, len(arr), subseq_len)]
    if len(set(subseqs)) != 6:
        return False
    
    # Check if the elements in each subsequence are in the required order
    for subseq in subseqs:
        if subseq != [4, 8, 15, 16, 23, 42]:
            return False
    
    return True

def remove_elements(arr):
    # Find the minimum number of elements to remove to make the array good
    min_elements = len(arr)
    for i in range(len(arr)):
        removed_elements = arr[:i] + arr[i + 1:]
        if is_good_array(removed_elements):
            min_elements = min(min_elements, len(removed_elements))
    
    return min_elements

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(remove_elements(arr))

