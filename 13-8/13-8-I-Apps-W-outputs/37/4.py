
def get_max_time(a, M):
    # Calculate the total time when the lamp is lit
    total_time = 0
    for i in range(len(a) - 1):
        total_time += a[i + 1] - a[i]
    total_time += M - a[-1]

    # Return the total time
    return total_time

def get_optimal_program(a, M):
    # Initialize the optimal program and its total time
    optimal_program = a
    optimal_time = get_max_time(a, M)

    # Iterate over all possible insertions
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            # Insert the value x at position j
            new_program = a[:j] + [x] + a[j:]

            # Calculate the total time for the new program
            new_time = get_max_time(new_program, M)

            # Update the optimal program and time if necessary
            if new_time > optimal_time:
                optimal_program = new_program
                optimal_time = new_time

    # Return the optimal program
    return optimal_program

def main():
    # Read the input
    n, M = map(int, input().split())
    a = list(map(int, input().split()))

    # Get the optimal program
    optimal_program = get_optimal_program(a, M)

    # Print the optimal time
    print(get_max_time(optimal_program, M))

if __name__ == '__main__':
    main()

