
def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

def solve(N, M, A):
    # Initialize variables
    max_days = 0
    current_day = 0
    assignment_days = [0] * M

    # Loop through each assignment
    for i in range(M):
        # Check if the current day is before the deadline
        if current_day < A[i]:
            # Add the current day to the assignment days
            assignment_days[i] += 1
            current_day += 1
        # If the current day is after the deadline, check if the assignment can be completed on the next day
        elif current_day == A[i]:
            # If the assignment can be completed on the next day, add the current day to the assignment days
            assignment_days[i] += 1
            current_day += 1
        # If the current day is after the deadline and the assignment cannot be completed on the next day, return -1
        else:
            return -1

    # Calculate the maximum number of days Takahashi can hang out
    max_days = N - sum(assignment_days)

    return max_days

def main():
    N, M, A = get_input()
    print(solve(N, M, A))

if __name__ == '__main__':
    main()

