
def get_min_cost(a):
    # Sort the list in ascending order
    a.sort()
    # Initialize the minimum cost to 0
    min_cost = 0
    # Loop through the list and calculate the cost of transforming each element
    for i in range(len(a) - 1):
        min_cost += (a[i] - a[i + 1]) ** 2
    # Return the minimum cost
    return min_cost

def main():
    # Read the input from stdin
    N = int(input())
    a = list(map(int, input().split()))
    # Call the get_min_cost function and print the result
    print(get_min_cost(a))

if __name__ == '__main__':
    main()

