
def get_magical_subarray(array, l, r):
    # Find the first and last element in the subarray
    first = array[l-1]
    last = array[r-1]
    
    # Initialize the longest subarray length to 0
    longest = 0
    
    # Iterate through the subarray
    for i in range(l, r+1):
        # If the current element is between the first and last element, increment the longest subarray length
        if first <= array[i-1] <= last:
            longest += 1
    
    return longest

def solve(array, queries):
    # Iterate through the queries
    for query in queries:
        # Get the longest subarray for the current query
        longest = get_magical_subarray(array, query[0], query[1])
        
        # Print the longest subarray length
        print(longest)

if __name__ == '__main__':
    # Read the input
    n = int(input())
    array = list(map(int, input().split()))
    q = int(input())
    queries = [[int(x) for x in input().split()] for _ in range(q)]
    
    # Solve the problem
    solve(array, queries)

