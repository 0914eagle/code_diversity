
def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

def solve(N, M, A):
    # Initialize variables
    max_days = 0
    current_day = 0
    assignment_days = []

    # Loop through each assignment
    for i in range(M):
        # Check if the current day is within the vacation days
        if current_day + A[i] <= N:
            # Add the current assignment to the list of assignment days
            assignment_days.append(current_day)
            # Update the current day
            current_day += A[i]
        else:
            # If the current day is not within the vacation days, return -1
            return -1

    # Sort the list of assignment days in ascending order
    assignment_days.sort()

    # Loop through each assignment day
    for i in range(len(assignment_days)):
        # Check if the current day is within the vacation days
        if assignment_days[i] + A[i] <= N:
            # Update the maximum number of days
            max_days = max(max_days, assignment_days[i] - current_day)
            # Update the current day
            current_day = assignment_days[i] + A[i]
        else:
            # If the current day is not within the vacation days, return -1
            return -1

    # Return the maximum number of days
    return max_days

def main():
    N, M, A = get_input()
    print(solve(N, M, A))

if __name__ == '__main__':
    main()

