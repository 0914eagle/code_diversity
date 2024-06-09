
def get_candy_distribution(a, b):
    # Initialize the distribution dictionary
    distribution = {}

    # Loop through the candies and assign them to the sibling with the highest value
    for i in range(len(a)):
        if a[i] >= b[i]:
            distribution[i] = "A"
        else:
            distribution[i] = "B"

    return "".join(distribution.values())

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Call the function to get the candy distribution
    distribution = get_candy_distribution(a, b)

    # Print the output
    print(distribution)

if __name__ == '__main__':
    main()

