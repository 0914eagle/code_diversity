
def get_good_sleeping_times(n, h, l, r, a):
    # Initialize a list to store the good sleeping times
    good_times = []
    
    # Iterate through the list of sleeping times
    for i in range(n):
        # Check if the current sleeping time is between l and r inclusive
        if l <= a[i] <= r:
            # If it is, add it to the list of good sleeping times
            good_times.append(a[i])
    
    # Return the length of the list of good sleeping times
    return len(good_times)

def main():
    # Read the input data
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_good_sleeping_times function and print the result
    print(get_good_sleeping_times(n, h, l, r, a))

if __name__ == '__main__':
    main()

