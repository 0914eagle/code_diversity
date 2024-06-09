
def get_max_hangout_days(vacation_days, assignments, assignment_days):
    # Sort the assignments by the number of days required to complete them
    sorted_assignments = sorted(assignments, key=lambda x: x[1], reverse=True)

    # Initialize the maximum number of days Takahashi can hang out to 0
    max_hangout_days = 0

    # Iterate through the assignments and calculate the maximum number of days Takahashi can hang out
    for assignment in sorted_assignments:
        # Check if the current assignment can be completed on the current day
        if vacation_days >= assignment[1]:
            # Subtract the number of days required to complete the current assignment from the total number of vacation days
            vacation_days -= assignment[1]
        else:
            # If the current assignment cannot be completed on the current day, break the loop
            break

    # Calculate the maximum number of days Takahashi can hang out by subtracting the total number of days spent on assignments from the total number of vacation days
    max_hangout_days = vacation_days - sum(assignment[1] for assignment in sorted_assignments)

    # Return the maximum number of days Takahashi can hang out
    return max_hangout_days

def main():
    # Read the number of vacation days and the number of assignments from standard input
    vacation_days, num_assignments = map(int, input().split())

    # Read the number of days required to complete each assignment from standard input
    assignments = []
    for _ in range(num_assignments):
        assignments.append(tuple(map(int, input().split())))

    # Calculate the maximum number of days Takahashi can hang out during the vacation
    max_hangout_days = get_max_hangout_days(vacation_days, assignments, assignment_days)

    # Print the maximum number of days Takahashi can hang out during the vacation
    print(max_hangout_days)

if __name__ == '__main__':
    main()

