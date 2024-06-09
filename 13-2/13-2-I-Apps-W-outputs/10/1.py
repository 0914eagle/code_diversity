
def get_minimum_sets(n, a):
    # Sort the array in descending order
    a.sort(reverse=True)
    
    # Initialize the minimum number of sets to 0
    min_sets = 0
    
    # Loop through the array and check if the current element is greater than the previous element
    for i in range(n-1):
        if a[i] > a[i+1]:
            # If the current element is greater than the previous element, increment the minimum number of sets
            min_sets += 1
    
    # Return the minimum number of sets
    return min_sets + 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_minimum_sets(n, a))

if __name__ == '__main__':
    main()

