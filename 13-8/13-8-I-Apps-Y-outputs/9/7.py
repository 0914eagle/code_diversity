
def get_maximum_candies(n, k):
    # Sort the candies in descending order
    candies = sorted(range(n), key=lambda x: -x)
    # Initialize the number of candies given to each kid as 0
    num_candies = [0] * k
    # Loop through the candies and give them to the kids
    for i in range(n):
        # Give the current candy to the kid with the minimum number of candies
        min_index = num_candies.index(min(num_candies))
        num_candies[min_index] += 1
        # If the current candy is the last one and the number of candies given to each kid is not equal,
        # then distribute the remaining candies equally among the kids
        if i == n - 1 and num_candies != [n // k] * k:
            num_candies = [n // k] * k
    # Return the maximum number of candies given to any kid
    return max(num_candies)

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(get_maximum_candies(n, k))

if __name__ == '__main__':
    main()

