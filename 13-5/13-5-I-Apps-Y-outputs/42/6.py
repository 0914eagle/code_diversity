
def get_max_gifts(d, k):
    # Sort the boxes by the number of candies in each box
    d.sort()
    # Initialize the maximum number of gifts as 0
    max_gifts = 0
    # Iterate over the boxes
    for i in range(len(d)):
        # Check if the current box is divisible by k
        if d[i] % k == 0:
            # If the current box is divisible by k, add it to the maximum number of gifts
            max_gifts += 1
        # Check if the current box is not divisible by k but the next box is divisible by k
        elif i < len(d) - 1 and d[i + 1] % k == 0:
            # If the current box is not divisible by k but the next box is divisible by k, add the current box and the next box to the maximum number of gifts
            max_gifts += 2
    return max_gifts

def main():
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    print(get_max_gifts(d, k))

if __name__ == '__main__':
    main()

