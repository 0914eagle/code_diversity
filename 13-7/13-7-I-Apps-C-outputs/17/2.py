
def get_magical_subarray(array, l, r):
    # Find the minimum and maximum values in the subarray
    min_val = min(array[l:r+1])
    max_val = max(array[l:r+1])
    
    # Initialize the length of the longest magical subarray as 0
    longest_magical_subarray = 0
    
    # Iterate through the subarray and check if the values are between the minimum and maximum values
    for i in range(l, r+1):
        if array[i] >= min_val and array[i] <= max_val:
            longest_magical_subarray = max(longest_magical_subarray, i-l+1)
    
    return longest_magical_subarray

def main():
    # Read the input data
    n = int(input())
    array = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    
    # Iterate through the queries and find the longest magical subarray for each query
    for query in queries:
        l, r = query
        print(get_magical_subarray(array, l, r))

if __name__ == '__main__':
    main()

