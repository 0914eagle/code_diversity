
def get_fence_posts(poles, n):
    # Sort the poles in non-decreasing order
    poles.sort()
    # Initialize the number of cuts to 0
    cuts = 0
    # Initialize the length of the fence posts to 0
    fence_posts = 0
    # Loop through the poles and calculate the number of fence posts that can be made from each pole
    for pole in poles:
        # Calculate the number of fence posts that can be made from the current pole
        posts = int(pole / n)
        # Add the number of fence posts to the total number of fence posts
        fence_posts += posts
        # If the number of fence posts is greater than the number of fence posts needed, calculate the number of cuts needed for the current pole
        if fence_posts > n:
            # Calculate the number of cuts needed for the current pole
            cuts += fence_posts - n
            # Subtract the number of fence posts that were made from the total number of fence posts
            fence_posts -= posts
    # Return the number of cuts needed to make the fence
    return cuts

def main():
    # Read the number of poles and the number of fence posts needed
    k, n = map(int, input().split())
    # Read the lengths of the poles
    poles = list(map(int, input().split()))
    # Call the get_fence_posts function to calculate the number of cuts needed
    cuts = get_fence_posts(poles, n)
    # Print the number of cuts needed
    print(cuts)

if __name__ == '__main__':
    main()

