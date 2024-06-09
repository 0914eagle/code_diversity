
def get_average_selection(N, A, x):
    # Calculate the sum of the integers written on the cards
    sum_x = sum(x)
    # Calculate the number of ways to select cards such that the average is exactly A
    num_ways = 0
    for i in range(1, N+1):
        # Calculate the average of the selected cards
        avg = sum_x / i
        # Check if the average is exactly A
        if avg == A:
            num_ways += 1
    return num_ways

def main():
    # Read the input from stdin
    N, A = map(int, input().split())
    x = list(map(int, input().split()))
    # Calculate the number of ways to select cards such that the average is exactly A
    num_ways = get_average_selection(N, A, x)
    # Print the number of ways
    print(num_ways)

if __name__ == '__main__':
    main()

