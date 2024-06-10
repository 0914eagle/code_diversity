
def get_maximum_m(a, k):
    # Initialize the maximum value of m(a)
    max_m = 0
    # Initialize the number of swaps
    num_swaps = 0
    # Sort the array a in non-decreasing order
    a.sort()
    # Loop through each element of the array a
    for i in range(len(a)):
        # If the current element is negative, flip it to positive
        if a[i] < 0:
            a[i] = -a[i]
            # Increment the number of swaps
            num_swaps += 1
        # If the number of swaps is greater than the maximum number of swaps, break the loop
        if num_swaps > k:
            break
    # Calculate the maximum value of m(a)
    max_m = sum(a)
    return max_m

def main():
    # Read the input n and k
    n, k = map(int, input().split())
    # Read the array a
    a = list(map(int, input().split()))
    # Get the maximum value of m(a)
    max_m = get_maximum_m(a, k)
    # Print the maximum value of m(a)
    print(max_m)

if __name__ == '__main__':
    main()

