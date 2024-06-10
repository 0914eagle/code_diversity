
def get_maximum_lit_time(a, M):
    # Initialize variables
    n = len(a)
    total_lit_time = 0
    current_state = True
    current_time = 0

    # Iterate through the program
    for i in range(n):
        # Calculate the time until the next transition
        time_until_next_transition = a[i] - current_time

        # Update the total lit time
        total_lit_time += time_until_next_transition * current_state

        # Flip the current state
        current_state = not current_state

        # Update the current time
        current_time = a[i]

    # Calculate the time until power off
    time_until_power_off = M - current_time

    # Update the total lit time
    total_lit_time += time_until_power_off * current_state

    return total_lit_time

def main():
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_lit_time(a, M))

if __name__ == '__main__':
    main()

