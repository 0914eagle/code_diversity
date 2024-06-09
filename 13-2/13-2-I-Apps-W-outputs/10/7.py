
def get_minimum_sets(n, a):
    # Sort the array in descending order
    a.sort(reverse=True)
    
    # Initialize the minimum number of sets to 0
    min_sets = 0
    
    # Loop through the array and count the number of sets needed
    for i in range(n):
        # If the current element is not 0, add 1 to the minimum number of sets
        if a[i] != 0:
            min_sets += 1
    
    return min_sets

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_minimum_sets(n, a))

if __name__ == '__main__':
    main()

