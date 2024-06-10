
def get_maximum_lit_time(a, M):
    # Initialize variables
    n = len(a)
    total_lit_time = 0
    max_lit_time = 0
    current_state = 1
    current_time = 0

    # Iterate through the program
    for i in range(n):
        # Calculate the time until the next event
        next_time = a[i]
        if next_time > current_time:
            # Calculate the lit time for the current segment
            lit_time = next_time - current_time
            total_lit_time += lit_time

            # Check if the current segment is the longest lit segment so far
            if lit_time > max_lit_time:
                max_lit_time = lit_time

        # Flip the current state
        current_state = 1 - current_state
        current_time = next_time

    # Calculate the total lit time
    total_lit_time += M - current_time

    return total_lit_time

def main():
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_lit_time(a, M))

if __name__ == '__main__':
    main()

