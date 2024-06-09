
def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

def solve(N, M, A):
    # Initialize variables
    max_days = 0
    curr_day = 0
    assignments_done = 0

    # Sort the assignments by deadline
    A.sort()

    # Loop through each day of the vacation
    for day in range(N):
        # If the current day is a day when an assignment is due, mark it as done
        if curr_day in A:
            assignments_done += 1

        # If all assignments are done, update the maximum number of days hanging out
        if assignments_done == M:
            max_days = max(max_days, day)

        # Increment the current day
        curr_day += 1

    # If all assignments are not done, return -1
    if assignments_done != M:
        return -1

    # Return the maximum number of days hanging out
    return max_days

def main():
    N, M, A = get_input()
    print(solve(N, M, A))

if __name__ == '__main__':
    main()

