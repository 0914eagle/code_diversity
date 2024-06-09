
def get_minimum_sets(n, a):
    # Sort the array in descending order
    a.sort(reverse=True)
    
    # Initialize the number of sets to 0
    sets = 0
    
    # Loop through the array and count the number of sets
    for i in range(n):
        # If the current element is greater than the previous element, increment the number of sets
        if i > 0 and a[i] > a[i-1]:
            sets += 1
    
    return sets

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_minimum_sets(n, a))

