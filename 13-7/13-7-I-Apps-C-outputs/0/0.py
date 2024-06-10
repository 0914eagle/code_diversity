
def get_expected_severity(bugs, hours, failure_factor):
    # Initialize variables
    total_severity = 0
    fixed_bugs = []

    # Loop through the hours
    for hour in range(hours):
        # Choose the bug to work on
        bug_to_work_on = choose_bug_to_work_on(bugs, fixed_bugs)

        # Fix the bug with probability p
        if random.random() < bug_to_work_on[1]:
            fixed_bugs.append(bug_to_work_on)
            total_severity += bug_to_work_on[2]

        # Reduce the fix probability of the bug
        bug_to_work_on[1] *= failure_factor

    return total_severity

def choose_bug_to_work_on(bugs, fixed_bugs):
    # Initialize variables
    max_value = 0
    chosen_bug = None

    # Loop through the bugs
    for bug in bugs:
        # Calculate the value of fixing the bug
        value = bug[1] * bug[2]

        # Check if the bug has already been fixed
        if bug in fixed_bugs:
            value = 0

        # Check if the value is greater than the current maximum
        if value > max_value:
            max_value = value
            chosen_bug = bug

    return chosen_bug

def main():
    # Read input
    num_bugs, num_hours, failure_factor = map(int, input().split())
    bugs = []
    for _ in range(num_bugs):
        fix_probability, severity = map(float, input().split())
        bugs.append([fix_probability, fix_probability, severity])

    # Calculate the expected severity
    expected_severity = get_expected_severity(bugs, num_hours, failure_factor)

    # Print output
    print(expected_severity)

if __name__ == '__main__':
    main()

