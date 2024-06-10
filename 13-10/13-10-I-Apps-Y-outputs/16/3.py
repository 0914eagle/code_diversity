
def is_good_array(arr):
    # Check if the length of the array is divisible by 6
    if len(arr) % 6 != 0:
        return False
    
    # Check if the array can be split into 6 subsequences of length 2
    subseqs = [arr[i:i+2] for i in range(0, len(arr), 2)]
    if len(subseqs) != 6:
        return False
    
    # Check if each subsequence is one of the required numbers
    for subseq in subseqs:
        if subseq not in [[4, 8], [15, 16], [23, 42]]:
            return False
    
    return True

def remove_min_elements(arr):
    # Find the minimum number of elements to remove to make the array good
    min_elements = 0
    while not is_good_array(arr):
        min_elements += 1
        arr.pop()
    
    return min_elements

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(remove_min_elements(arr))

if __name__ == '__main__':
    main()

