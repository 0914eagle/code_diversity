
def get_minimum_sets(n, a):
    # Sort the input array in descending order
    a.sort(reverse=True)
    
    # Initialize the minimum number of sets to 0
    min_sets = 0
    
    # Loop through the input array
    for i in range(n):
        # If the current element is greater than the previous element, increase the minimum number of sets by 1
        if i > 0 and a[i] > a[i-1]:
            min_sets += 1
    
    # Return the minimum number of sets
    return min_sets

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_minimum_sets(n, a))

