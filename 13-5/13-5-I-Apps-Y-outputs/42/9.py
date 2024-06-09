
def get_max_gifts(n, k, d):
    # Sort the boxes by the number of candies in descending order
    sorted_boxes = sorted(d, reverse=True)

    # Initialize the maximum number of gifts as 0
    max_gifts = 0

    # Iterate over the boxes
    for i in range(n):
        # Check if the current box is divisible by k
        if sorted_boxes[i] % k == 0:
            # If the current box is divisible by k, increment the maximum number of gifts
            max_gifts += 1

    return max_gifts

def main():
    # Read the input
    n, k = map(int, input().split())
    d = list(map(int, input().split()))

    # Call the get_max_gifts function and print the result
    print(get_max_gifts(n, k, d))

if __name__ == '__main__':
    main()

