
def get_min_cuts(poles, n):
    # Sort the poles in non-decreasing order
    poles.sort()
    # Initialize the number of cuts as 0
    cuts = 0
    # Loop through each pole and check if it is greater than or equal to the length of the fence
    for pole in poles:
        if pole >= n:
            # If the pole is greater than or equal to the length of the fence, we can use it as a fence post
            # and increment the number of cuts by 1
            cuts += 1
            # Decrement the length of the fence by the length of the pole
            n -= pole
        else:
            # If the pole is less than the length of the fence, we cannot use it as a fence post
            # and break the loop
            break
    # Return the number of cuts needed to build the fence
    return cuts

def main():
    # Read the input data
    k, n = map(int, input().split())
    poles = list(map(int, input().split()))
    # Call the get_min_cuts function and print the result
    print(get_min_cuts(poles, n))

if __name__ == '__main__':
    main()

